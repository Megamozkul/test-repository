import sys
from pathlib import Path
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier 

def main():
   
    if len(sys.argv) < 5:
        print("Usage: python gradient_boosting.py <train_path> <test_path> <output_path> <target> <feature1> [feature2] ...")
        sys.exit(1)

    train_path = Path(sys.argv[1])
    test_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    target = sys.argv[4]
    features = sys.argv[5:]

  
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)


    missing_features = [f for f in features if f not in train.columns]
    if missing_features:
        raise ValueError(f"Отсутствуют признаки в train: {missing_features}. Доступные: {list(train.columns)}")
    if target not in train.columns:
        raise ValueError(f"Целевая колонка '{target}' не найдена. Доступные: {list(train.columns)}")

    X_train = train[features]
    y_train = train[target]
    X_test = test[features]


    model = GradientBoostingClassifier(
        n_estimators=100,         
        learning_rate=0.1,       
        max_depth=3,          
        random_state=42,          
        min_samples_leaf=5,      
        subsample=0.8            
    )
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    pd.DataFrame({"target": y_pred}).to_csv(output_path, index=False)
    print(f"Результаты градиентного бустинга сохранены в: {output_path}")

if __name__ == "__main__":
    main()