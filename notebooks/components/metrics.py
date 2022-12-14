import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd


def calculate_regression_metrics(actuals, fitted):
    error = actuals - fitted
    mae = (abs(error).sum()) / len(error)
    mse = ((error ** 2).sum()) / len(error)
    mape = ((abs(error / actuals).sum()) / len(error)) * 100
    rmse = np.sqrt(mse)
    mpe = ((error / actuals).sum()) / len(error) * 100
    return mae, mse, mape, rmse, mpe


def print_model_metrics(x_train, y_train, y_pred):
    mae, mse, mape, rmse, mpe = calculate_regression_metrics(y_train, y_pred)
    train_df = pd.DataFrame(pd.concat([x_train, y_train], axis=1))
    print("Coefficient of determination (R squared): \t %.2f" % r2_score(
        y_train, y_pred))
    print("Correlation with pearson coefficient \t %.2f " % train_df.corr(
        method="pearson").iloc[0, 1])
    print("Correlation with spearman coefficient \t %.2f " % train_df.corr(
        method="spearman").iloc[0, 1])
    print("Mape absolute percentage error: \t %.2f " % mape)
    print("Mean squared error: \t %.2f " % mean_squared_error(y_train, y_pred))
    df = pd.DataFrame(
        data=[
            r2_score(y_train, y_pred),
            train_df.corr(method="pearson").iloc[0, 1],
            train_df.corr(method="spearman").iloc[0, 1],
            mape,
    ],
        index=["Coefficient of determination (R Squared)",
               "Correlation with pearson coefficient",
               "Correlation with spearman coefficient",
               "Mean squared error"
               ]
    )
    return df