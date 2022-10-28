""" Welcome to Meta!
This is just a simple shared plaintext pad,
with no execution capabilities.

When you know what language you would like
to use for your interview, simply choose it
from the dropdown in the top bar.

Enjoy your interview!

# question 1

Given a string of characters, write a method that returns
true if the string represents a valid number.

"13" - --> true
"3.0" - --> true
"-7.4" - --> true
"-13.5" - --> true
"abc" - --> false
"123a" - --> false
"-." - --> false
"-..--" - --> false
"1.0.0.1" -> false

"""
import pandas as pd


def check_string_ints(s: str) -> bool:
    for i in s:
        try:
            char = int(s[i])
        except error as e:
            print(f"found a string not int {e}")
        if type(char) == int:
            return True
        else:
            return False


def check_string_int(s: str) -> bool:  # "123a" # 3.0"
    n = len(s)
    sub = s[0]  # '3'
    for i in s:  # 1
        if int(sub):  # int('3.5')
            sub += s[i + 1]  # '3.'
            result = True
        else:
            return False
        return result


"""
#question 2

Given the coordinates of a facebook user and some
shops, return the k shops closest to the user

Input:
user = (3, 1)
k = 2
shops = ("A", 3, 3), ("B", 9, 1)("C", 4, 2)

Output: ["A", "C"]

// |
// | A
// | C
// | *B
// --o - -----------
// |
"""
from math import sqrt


def euclidean_distance(a, b, c, d):
    return sqrt((a - c) ^ 2 + (b - d) ^ 2)


user = (3, 1)
shops = [("A", 3, 3), ("B", 9, 1), ("C", 4, 2), ("Z", 1, 2)]


def find_closest_k_shops(k, person, location):
    shop_dict = {}
    # i=o ("A",3,3)
    for i in location:  # euclidean_distance(3, 1, 3, 3)
        shop_dict[location[i][0]] = euclidean_distance(
            *person, *location[i][1:2]
        )  # location[i][0] ="A" 3, 1 location[i][1:2]=(3,3) 3, 3
    df = pd.DataFrame(shop_dict)
    sorted_values = sorted(df.values)
    return list(sorted_values.index[k])


x = find_closest_k_shops(5, user, shops)
