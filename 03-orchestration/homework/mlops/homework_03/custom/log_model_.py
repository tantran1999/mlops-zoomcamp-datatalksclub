from typing import Tuple
import pickle
import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def log_model(data: Tuple[LinearRegression, DictVectorizer], *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    model = data[0]
    dict_vectorizer = data[1]

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("homework_03")

    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="sklearn-model",
        registered_model_name="homework-03-trained-model",
    )

    with open("dict_vectorizer.pkl", "wb") as f:
        pickle.dump(dict_vectorizer, f)
    mlflow.log_artifacts("dict_vectorizer.pkl")
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
