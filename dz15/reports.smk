rule calculate_scores:
    input:
        "data/processed/test_titanic.csv",      # test_data
        "forecast/logistic_regression_titanic.csv"  # predictions
    output:
        "reports/calculate_scores_titanic.csv"
    shell:
        """
        python reports/calculate_accuracy.py {input} {output}
        """

rule calculate_all_scores:
    input:
        test_data="data/processed/test_titanic.csv",
        logit_pred="forecast/logistic_regression_titanic.csv",
        gb_pred="forecast/gradient_boosting_titanic.csv"
    output:
        "reports/all_scores_titanic.csv"
    shell:
        """
        python reports/calculate_all_accuracy.py {input[test_data]} {input[logit_pred]} {input[gb_pred]} {output}
        """