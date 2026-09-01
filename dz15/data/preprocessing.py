import sys
from pathlib import Path
import pandas as pd

def main():
    if len(sys.argv) < 5:
        print("Usage: python data/preprocessing.py <input_path> <output_path> <preproc_type> <target_col> [feature1] ...")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    preproc_type = sys.argv[3]
    target_col = sys.argv[4]
    features = sys.argv[5:]

    df = pd.read_csv(input_path)

    # Кодирование Sex
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    # Заполнение пропусков Age
    df['Age'] = df['Age'].fillna(
        df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
    )

    # Масштабирование только для варианта "scaled"
    if preproc_type == "scaled":
        mean = df[features].values.mean()
        std = df[features].values.std()
        df[features] = (df[features] - mean) / std
        print(f"Применено масштабирование (StandardScaler) к: {features}")
    else:
        print("Масштабирование пропущено (standard)")

    df.to_csv(output_path, index=False)
    print(f"Предобработанные данные ({preproc_type}) сохранены в: {output_path}")

if __name__ == "__main__":
    main()