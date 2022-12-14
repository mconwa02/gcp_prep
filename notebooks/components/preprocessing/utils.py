import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def null_values_df(df):
    df = df.copy()
    age_mapping = {27: np.nan, 35: np.nan}
    salary_mapping = {"Annual": np.nan}
    df['AGE'] = df['AGE'].replace(age_mapping)
    df['EMP_SAL_FRQ'] = df['EMP_SAL_FRQ'].replace(salary_mapping)
    df['EMP_ID'] = np.nan
    return df


def selected_variables(df, col):
    df[col].hist(grid=False, bins=30).plot()
    plt.title(col)
    plt.show()
    print(df[col].describe())


def emp_convert_string(df):
    df = df.copy()
    sal_mapping = {"Annual": 0, "Monthly": 2, "Weekly": 1}
    emp_mapping = {"FT": 3, "PT": 2, "UN": 1, "STU": 0, "RT": 1, "SLF": 0}
    df["EMP_TYP"] = df["EMP_TYP"].replace(emp_mapping)
    df["EMP_SAL_FRQ"] = df["EMP_SAL_FRQ"].replace(sal_mapping)
    df = pd.get_dummies(df, columns=["EMP_TYP", "EMP_SAL_FRQ"])
    return df



