rule calculate_scores:
    input:
        test_data="data/processed/test_{preproc}.csv",
        pred="forecast/logistic_regression_{preproc}.csv"
    output:
        "reports/calculate_scores_{preproc}.csv"
    shell:
        """
        python reports/calculate_accuracy.py {input.test_data} {input.pred} {output}
        """


rule calculate_all_scores:
    input:
        test_data="data/processed/test_{preproc}.csv",
        logit_pred="forecast/logistic_regression_{preproc}.csv",
        gb_pred="forecast/gradient_boosting_{preproc}.csv",
        rf_pred="forecast/random_forest_{preproc}.csv"
    output:
        "reports/all_scores_{preproc}.csv"
    shell:
        """
        python reports/calculate_all_accuracy.py \
            {input.test_data} \
            {input.logit_pred} \
            {input.gb_pred} \
            {input.rf_pred} \
            {output}
        """


rule compare_preprocessing:
    input:
        standard="reports/all_scores_standard.csv",
        scaled="reports/all_scores_scaled.csv"
    output:
        "reports/comparison_titanic.csv"
    shell:
        """
        python reports/compare_preprocessing.py {input.standard} {input.scaled} {output}
        """