from pandas import DataFrame
import pytest

from feature_engineering import categorical_feature_to_dict, check_if_categorical


@pytest.fixture
def test_dataframe():
    return DataFrame(data=["A", "A", "B"], columns=["feature"])


def test_categorical_feature_to_dict(test_dataframe):
    # df = DataFrame(data=["A", "A", "B"], columns=["feature"])
    actual_dict = categorical_feature_to_dict(test_dataframe, "feature")
    expected_dict = {"A": 2, "B": 1}
    assert actual_dict == expected_dict


def test_check_if_categorical():
    check_if_categorical(test_dataframe, "feature")
