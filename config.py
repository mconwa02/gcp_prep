# https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales

DATA_PATH = r"C:\dev\data\gcp_prep\supermarket_sales.csv"
TARGET = "RATING"
FEATURES = [
    "INVOICE_ID",
    "BRANCH",
    "CITY",
    "CUSTOMER_TYPE",
    "GENDER",
    "PRODUCT_LINE",
    "UNIT_PRICE",
    "QUANTITY",
    "TAX",
    "TOTAL",
    "DATE",
    "TIME",
    "PAYMENT",
    "COST_OF_GOODS_SOLD",
    "GROSS_MARGIN_PERCENTAGE",
    "GROSS_INCOME",
]
TRAIN_TEST_SPLIT = 0.30
