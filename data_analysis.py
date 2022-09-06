import pandas as pd
import logging
from notebooks.config import DATA_PATH, TRAIN_TEST_SPLIT
from cross_validation import k_fold_cross_validation
from features import FEATURE_DICT

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_kaggle_data():
    df = pd.read_csv(DATA_PATH)
    logger.info(df.info())
    # summary df descriptive statistics
    print(df.describe())
    print(df.select_dtypes(include="object"))

    df.rename(columns=FEATURE_DICT, inplace=True)

    x_train, x_test, y_train, y_test = k_fold_cross_validation(df, TRAIN_TEST_SPLIT)


if __name__ == "__main__":
    read_kaggle_data()
