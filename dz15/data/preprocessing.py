
import sys
from pathlib import Path
import pandas as pd

def main():

    if len(sys.argv) < 4:
        print("Usage: python data/preprocessing.py <input_path> <output_path> <target_col> <feature1> [feature2] ...")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    target_col = sys.argv[3]
    features = sys.argv[4:]

    df = pd.read_csv(input_path)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Age'] = df['Age'].fillna(
        df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
    )

    mean = df[features].values.mean()
    std = df[features].values.std()
    df[features] = (df[features] - mean) / std

    df.to_csv(output_path, index=False)
    print(f"Предобработанные данные сохранены в: {output_path}")

if __name__ == "__main__":
    main()