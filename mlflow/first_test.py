# This is a modified version of the sample from the MLFlow documentation
# Source: https://www.mlflow.org/docs/latest/quickstart.html

import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import mlflow

if __name__ == "__main__":
    mlflow.set_experiment(experiment_name='First Experiment')

    with mlflow.start_run(run_name='test_run'):
        # Log a parameter (key-value pair)
        log_param("param_1", randint(0, 100))

        # Log a metric; metrics can be updated throughout the run
        log_metric("metric_1", random())
        log_metric("metric_1", random() + 1)
        log_metric("metric_1", random() + 2)

        # You can add another metric
        log_metric("metric_2", random() + 2)

        # Log an artifact (output file)
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open("outputs/test.txt", "w") as f:
            f.write("hello world!")
        log_artifacts("outputs")

