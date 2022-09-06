import logging

from sklearn.model_selection import train_test_split

from notebooks.config import FEATURES, TARGET

logger = logging.getLogger(__name__)


def k_fold_cross_validation(df, train_size):
    x_train, x_test, y_train, y_test = train_test_split(
        df[FEATURES], df[TARGET], random_state=1, train_size=train_size
    )
    logger.info(f"x_train has {x_train.shape[0]} rows and {x_train.shape[1]} columns")
    logger.info(f"y_train has {y_train.shape[0]} rows and 1 columns")
    logger.info(f"x_test has {x_test.shape[0]} rows and {x_test.shape[1]} columns")
    logger.info(f"y_test has {y_test.shape[0]} rows and 1 columns")
    return x_train, x_test, y_train, y_test
