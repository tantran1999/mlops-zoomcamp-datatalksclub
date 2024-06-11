import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def log_model(model: LinearRegression, dict_vectorizer: DictVectorizer, *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("homework_03")

    mlflow.log_model()

    
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
