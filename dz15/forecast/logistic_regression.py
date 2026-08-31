import sys
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression

def main():
    if len(sys.argv) < 5:
        print("Usage: python logistic_regression.py <train_path> <test_path> <output_path> <target> <feature1> [feature2] ...")
        sys.exit(1)

    train_path = Path(sys.argv[1])
    test_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    target = sys.argv[4]
    features = sys.argv[5:]


    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    # Проверка колонок
    missing_features = [f for f in features if f not in train.columns]
    if missing_features:
        raise ValueError(f"Отсутствуют признаки в train: {missing_features}. Доступные: {list(train.columns)}")
    if target not in train.columns:
        raise ValueError(f"Целевая колонка '{target}' не найдена в train. Доступные: {list(train.columns)}")

    x_train = train[features]
    y_train = train[target]
    x_test = test[features]

    # Обучение модели
    model = LogisticRegression(max_iter=3000)
    model.fit(x_train, y_train)

    # Предсказание
    y_pred = model.predict(x_test)

    # Сохранение результатов
    pd.DataFrame({"target": y_pred}).to_csv(output_path, index=False)
    print(f"Результаты предсказаний сохранены в: {output_path}")

if __name__ == "__main__":
    main()