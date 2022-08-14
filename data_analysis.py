import pandas as pd

from config import DATA_PATH


def read_kaggle_data():
    df = pd.read_csv(DATA_PATH)
    print(df.info())
    # summary df descriptive statistics
    print(df.describe())
    print(df.select_dtypes(include='object'))





if __name__ == "__main__":
    read_kaggle_data()
