
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
    COGS = "cogs"
    GROSS_MARGIN_PERCENTAGE = "gross margin percentage"
    GROSS_INCOME = "gross income"
    RATING = "Rating"
