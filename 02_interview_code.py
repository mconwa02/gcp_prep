# Assuming you have the following data with X as a feature and Y as the target.
# You fit both a Linear Regression and a Decision Tree.
# What is going to be the output then predicting lm.predict(x=0.5) and tree.predict(x=0.5)?
"""
X, Y
0, 0
1, 1
"""

# You want to create a function to sum all the multiple of 3 or 5 for all the first 1,000 numbers.
import pandas as pd


def sum_multiples(N: int):
    # list = [x if (x % 3 == 0) & (x % 5 ==0) for x in range(N)]
    other_list = list()
    for x in range(N):
        if x % 3 == 0 or x % 5:  # 15
            other_list.append(x)
    return pd.Series(other_list).sum()


print(sum_multiples(1000))

N = 1000


def sum_single_multiple(N: int, multiple: int) -> int:
    loops = N / multiple
    final_list = []
    for x in range(loops):
        final_list.append(x * multiple)
    return pd.Series(final_list).sum()


print(f"the sum of 5 multiples from {N} values: { sum_single_multiple(1000, 5)}")
print(f"the sum of 3 multiples from {N} values: { sum_single_multiple(1000, 3)}")

sum_both = sum_single_multiple(1000, 5) + sum_single_multiple(1000, 3)

isinstance(sum_multiples(1000), sum_both)


def sum_sinle_multiple(N: int) -> int:
    loops = N / 3
    list_5 = []
    list_3 = []
    for x in range(loops):
        list_3.append(x * 3)
    for x in range(200):
        list_5.append(x * 5)
    final_set = set(list_3 + list(5))
    return pd.Series(final_set).sum()


# You have the following data - how are encoding the categorical variables to make it usable for a LinearRegression?
"""

customer_id, date, gender, country, revenue_last_12m
0, 1/1/2021, F, italy, $100
1, 1/1/2021, F, UK, $1000
2, 1/3/2021, M, UK, $50
3, 1/4/2021, M, Germany, $800
0, 1/6/2021, F, italy, $300

"""