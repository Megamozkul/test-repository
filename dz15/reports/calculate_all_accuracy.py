import sys
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import psycopg2


def save_metrics_to_db(df_res):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="mysecretpassword",
        dbname="postgres",
    )
    cur = conn.cursor()
    for _, row in df_res.iterrows():
        cur.execute(
            """
            INSERT INTO model_metrics (model_name, accuracy, precision, recall, f1_score)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                row["model"],
                row["accuracy"],
                row["precision_macro"],
                row["recall_macro"],
                row["f1_macro"],
            ),
        )
    conn.commit()
    cur.close()
    conn.close()
    print("Метрики сохранены в БД.")


def main():
    if len(sys.argv) != 6:
        print("Usage: python calculate_all_accuracy.py <test_path> <logit_pred_path> <gb_pred_path> <rf_pred_path> <output_path>")
        print(f"Получено аргументов: {len(sys.argv) - 1}")
        sys.exit(1)

    test_path = Path(sys.argv[1])
    logit_path = Path(sys.argv[2])
    gb_path = Path(sys.argv[3])
    rf_path = Path(sys.argv[4])
    out_path = Path(sys.argv[5])

    # Читаем данные
    test = pd.read_csv(test_path)
    logit = pd.read_csv(logit_path)
    gb = pd.read_csv(gb_path)
    rf = pd.read_csv(rf_path)

    # Проверка колонок
    if "Survived" not in test.columns:
        raise ValueError(f"В тестовом датасете нет колонки 'Survived'. Есть: {list(test.columns)}")
    for name, df in [("logit", logit), ("gb", gb), ("rf", rf)]:
        if "target" not in df.columns:
            raise ValueError(f"В файле {name} нет колонки 'target'. Есть: {list(df.columns)}")

    y_true = test["Survived"]
    y_logit = logit["target"]
    y_gb = gb["target"]
    y_rf = rf["target"]

    def get_metrics(y_true, y_pred, name):
        acc = accuracy_score(y_true, y_pred)
        report = classification_report(y_true, y_pred, output_dict=True)
        return {
            "model": name,
            "accuracy": acc,
            "precision_macro": report["macro avg"]["precision"],
            "recall_macro": report["macro avg"]["recall"],
            "f1_macro": report["macro avg"]["f1-score"],
        }

    rows = [
        get_metrics(y_true, y_logit, "logistic_regression"),
        get_metrics(y_true, y_gb, "gradient_boosting"),
        get_metrics(y_true, y_rf, "random_forest"),
    ]

    df_res = pd.DataFrame(rows)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_res.to_csv(out_path, index=False)
    print(f"Сводный отчёт сохранён в: {out_path}")

    # Запись в БД — не роняем пайплайн, если БД недоступна
    try:
        save_metrics_to_db(df_res)
    except Exception as e:
        print(f"Предупреждение: не удалось записать в БД ({e}). CSV сохранён.")


if __name__ == "__main__":
    main()