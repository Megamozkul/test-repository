import sys
from pathlib import Path
import pandas as pd

def main():
    if len(sys.argv) != 4:
        print("Usage: python data/download.py <input_path> <output_path> <target_column>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    target = sys.argv[3]


    df = pd.read_csv(input_path)


    if target not in df.columns:
        raise ValueError(
            f"Целевая колонка '{target}' не найдена. "
            f"Доступные колонки: {list(df.columns)}"
        )


    df.to_csv(output_path, index=False)
    print(f"Датасет сохранён в: {output_path}")

if __name__ == "__main__":
    main()