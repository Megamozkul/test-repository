from snake_config import raw_path, interim_path, processed_path


rule download_data:
    input:
        "data/raw/train.csv"
    output:
        "data/interim/dataset_titanic.csv"
    params:
        target="Survived"
    shell:
        """
        python data/download.py {input} {output} {params.target}
        """


rule preprocessing_data:
    input:
        "data/interim/dataset_titanic.csv"
    output:
        "data/processed/preprocessing_dataset_{preproc}.csv"
    params:
        preproc="{preproc}",
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python data/preprocessing.py {input} {output} {params.preproc} {params.target} {params.features}
        """


rule train_test_split:
    input:
        "data/processed/preprocessing_dataset_{preproc}.csv"
    output:
        train="data/processed/train_{preproc}.csv",
        test="data/processed/test_{preproc}.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python data/train_test_split.py {input} {output.train} {output.test} {params.target} {params.features}
        """