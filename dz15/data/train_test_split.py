import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    if len(sys.argv) < 5:
        print("Usage: python data/train_test_split.py <input_path> <output_train_path> <output_test_path> <target> <feature1> [feature2] ...")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_train_path = Path(sys.argv[2])
    output_test_path = Path(sys.argv[3])
    target = sys.argv[4]
    features = sys.argv[5:]

    df = pd.read_csv(input_path)

    # Проверка наличия необходимых столбцов
    missing_features = [f for f in features if f not in df.columns]
    if missing_features:
        raise ValueError(f"Отсутствуют признаки в датасете: {missing_features}. Доступные: {list(df.columns)}")

    if target not in df.columns:
        raise ValueError(f"Целевая колонка '{target}' не найдена. Доступные: {list(df.columns)}")

    x_train, x_test, y_train, y_test = train_test_split(
        df[features],
        df[target],
        train_size=0.8,
        random_state=42
    )

    train = pd.concat([x_train, y_train], axis=1)
    test = pd.concat([x_test, y_test], axis=1)

    train.to_csv(output_train_path, index=False)
    test.to_csv(output_test_path, index=False)

    print(f"Train сохранён в: {output_train_path}")
    print(f"Test сохранён в: {output_test_path}")

if __name__ == "__main__":
    main()