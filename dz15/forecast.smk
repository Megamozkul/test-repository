rule logistic_regression_forecast:
    input:
        "data/processed/train_titanic.csv",
        "data/processed/test_titanic.csv"
    output:
        "forecast/logistic_regression_titanic.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python forecast/logistic_regression.py {input} {output} {params.target} {params.features}
        """

rule gradient_boosting_forecast:
    input:
        "data/processed/train_titanic.csv",
        "data/processed/test_titanic.csv"
    output:
        "forecast/gradient_boosting_titanic.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python forecast/gradient_boosting.py {input} {output} {params.target} {params.features}
        """