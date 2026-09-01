import sys
from pathlib import Path
import pandas as pd

def main():
    if len(sys.argv) != 4:
        print("Usage: python compare_preprocessing.py <standard_scores> <scaled_scores> <output>")
        sys.exit(1)

    standard_path = Path(sys.argv[1])
    scaled_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    df_standard = pd.read_csv(standard_path)
    df_scaled = pd.read_csv(scaled_path)

    df_standard["preprocessing"] = "standard"
    df_scaled["preprocessing"] = "scaled"

    df_all = pd.concat([df_standard, df_scaled], ignore_index=True)
    df_all = df_all.sort_values("accuracy", ascending=False).reset_index(drop=True)
    df_all["rank"] = df_all["accuracy"].rank(ascending=False, method="min").astype(int)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_all.to_csv(output_path, index=False)

    print("\n=== Сравнение моделей и вариантов предобработки ===\n")
    print(df_all[["rank", "model", "preprocessing", "accuracy", "precision_macro", "recall_macro", "f1_macro"]].to_string(index=False))
    best = df_all.iloc[0]
    print(f"\nЛучший результат: {best['model']} + {best['preprocessing']} (accuracy = {best['accuracy']:.4f})\n")

if __name__ == "__main__":
    main()