from enum import Enum

# The dir() function prints all of the attributes of a Python object.
# The vars() function object’s instance attributes as well as their values.


class AvailableFeatures(Enum):
    INVOICE_ID = "Invoice ID"
    BRANCH = "Branch"
    CITY = "City"
    CUSTOMER_TYPE = "Customer type"
    GENDER = "Gender"
    PRODUCT_LINE = "Product line"
    UNIT_PRICE = "Unit price"
    QUANTITY = "Quantity"
    TAX = "Tax 5%"
    TOTAL = "Total"
    DATE = "Date"
    TIME = "Time"
    PAYMENT = "Payment"
    COST_OF_GOODS_SOLD = "cogs"
    GROSS_MARGIN_PERCENTAGE = "gross margin percentage"
    GROSS_INCOME = "gross income"
    RATING = "Rating"


FEATURE_DICT = {
    "Invoice ID": "INVOICE_ID",
    "Branch": "BRANCH",
    "City": "CITY",
    "Customer type": "CUSTOMER_TYPE",
    "Gender": "GENDER",
    "Product line": "PRODUCT_LINE",
    "Unit price": "UNIT_PRICE",
    "Quantity": "QUANTITY",
    "Tax 5%": "TAX",
    "Total": "TOTAL",
    "Date": "DATE",
    "Time": "TIME",
    "Payment": "PAYMENT",
    "cogs": "COST_OF_GOODS_SOLD",
    "gross margin percentage": "GROSS_MARGIN_PERCENTAGE",
    "gross income": "GROSS_INCOME",
    "Rating": "RATING",
}
