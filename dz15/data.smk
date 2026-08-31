from snake_config import raw_path,interim_path,processed_path


rule download_data:
    input:
        "data/raw/train.csv"
    output:
        "data/interim/dataset_titanic.csv"
    params:
        target="Survived"   # имя целевой колонки из твоего CSV
    shell:
        """
        python data/download.py {input} {output} {params.target}
        """


rule preprocessing_data:
    input:
        "data/interim/dataset_titanic.csv"
    output:
        "data/processed/preprocessing_dataset_titanic.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python data/preprocessing.py {input} {output} {params.target} {params.features}
        """

rule train_test_split:
    input:
        "data/processed/preprocessing_dataset_titanic.csv"
    output:
        "data/processed/train_titanic.csv",
        "data/processed/test_titanic.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python data/train_test_split.py {input} {output} {params.target} {params.features}
        """
