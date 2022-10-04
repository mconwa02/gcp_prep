def say_hello():
    print('Hello, World')


for i in range(5):
    say_hello()


# Determine if any 3 integers in an array sum to 0.

# [1 2 3 -4] => True
# [1 -1 10 100] => False


def sum_intergers(array: list) -> bool:  # [1 2 3 -4]
    N = len(array)  # 4
    sum_3 = 0
    for i in range(N):  # 0
        for j in range(N):  # 0
            for k in range(N):  # 0
                if (i != j) & (j != k) & (i != k) & (array[i] + array[j] + array[k] == 0):  # False
                    return True
    return False


sum_intergers([3, 4, 5, 6, 7, 3, 5, 3, 4, -3, -4, -5])

# 1 11 21 1211 111221 312211 13112221 1113213211 31131211131221 13211311123113112211
# You get a new sequence from the old one by saying what you see. I.e. 1 <- initial sequence 11 <- 1 x 1 (you see one one)
# 21 <- 2 x 1 (you see two ones) 1211 <- 1x2 1x1 (you see one two, and two ones)
from collection import Counter


def create_sequence(number: int):  # 1
    string_num = str(number)  # '1'
    count = 0
    other_count = 0
    result = string_num[0]  # '1'
    if result > 1:
        for i in range(len(string_num) - 1):  # 0
            if string_num[i] == string_num[i + 1]:
                count += 1
                result += str(count) + str(string_num[i])
            else:
                other_count += 1
                result += str(other_count) + str(string_num[i])


return result

# num_dict = Counter(string_num)
# for key, val in num_dict.items():