from typing import Dict

from pandas import DataFrame


def check_if_categorical(df, feature):
    try:
        type(df[feature]) == object
    except KeyError:
        print("This feature is not a categorical feature")


def categorical_feature_to_dict(df: DataFrame, feature: str) -> Dict:
    """
    The function creates a dictionary of a features
    :param df:
    :param feature:
    :return: dictonary of features values
    """
    check_if_categorical(df, feature)
    return df[feature].value_counts().to_dict()
