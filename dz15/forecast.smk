rule logistic_regression_forecast:
    input:
        train="data/processed/train_{preproc}.csv",
        test="data/processed/test_{preproc}.csv"
    output:
        "forecast/logistic_regression_{preproc}.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python forecast/logistic_regression.py {input.train} {input.test} {output} {params.target} {params.features}
        """


rule gradient_boosting_forecast:
    input:
        train="data/processed/train_{preproc}.csv",
        test="data/processed/test_{preproc}.csv"
    output:
        "forecast/gradient_boosting_{preproc}.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python forecast/gradient_boosting.py {input.train} {input.test} {output} {params.target} {params.features}
        """


rule random_forest_forecast:
    input:
        train="data/processed/train_{preproc}.csv",
        test="data/processed/test_{preproc}.csv"
    output:
        "forecast/random_forest_{preproc}.csv"
    params:
        target="Survived",
        features=["Pclass", "Sex", "Age"]
    shell:
        """
        python forecast/random_forest_titanic.py {input.train} {input.test} {output} {params.target} {params.features}
        """