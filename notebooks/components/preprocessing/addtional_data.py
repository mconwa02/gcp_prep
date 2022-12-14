from datetime import date

import pandas as pd
import numpy as np


def format_data(df):
    df = df.copy()
    sex_mapping = {"female": 0, "male": 1}
    smoker_mapping = {"no": 0, "yes": 1}
    region_df = pd.get_dummies(df[["region"]])
    df = pd.concat([df, region_df], axis=1)
    df["smoker"] = df["smoker"].replace(smoker_mapping)
    df["REGION"] = df.region
    df["AGE"] = df.age.astype(int)
    df["CUS_ID"] = range(1, df.shape[0] + 1)
    df["EMP_ID"] = np.random.randint(10, 500, df.shape[0])
    df["ADDRESS_ID"] = np.random.randint(5000, 10_000, df.shape[0])
    df["DOB_DT"] = [date(1920, 1, 1)] * df.shape[0]
    df["VALID_FR_DT"] = [date(1920, 1, 1)] * df.shape[0]
    df["VALID_FR_DT"] = [date(1920, 1, 1)] * df.shape[0]
    df["EMP_TYP"] = np.random.choice(
        ["FT", "PT", "UN", "STU", "RT", "SLF"],
        df.shape[0],
        p=[0.2, 0.2, 0.2, 0.2, 0.1, 0.1],
    )
    df["EMP_SAL_FRQ"] = np.random.choice(
        ["Annual", "Monthly", "Weekly"],
        df.shape[0],
        p=[0.2, .4, .4],
    )
    df["SEX_CD"] = 1
#     df["SEX_CD"].iloc[-250] = df.gender.replace(sex_mapping).iloc[-250:]
    df["DEPEND_CNT"] = df["children"]
#     df[df["SEX_CD"] == 0].iloc[-250:]["SEX_CD"] = 1
    df["TARGET"] = df.charges
    return df

