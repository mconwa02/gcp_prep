from typing import List


class NumArray:
    """
    Given an integer array nums

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_array = 0
        for i in range(right-left + 1):
            sum_array += self.nums[left + i]
        return sum_array


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class OnlineSolution:
    def read(self, buf: List[str], n: int) -> int:
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4

        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)

            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1

        return copied_chars


class Solution:

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        num = 0
        buf4 = ''
        for i in range(len(buf)):
            buf4 += buf[i]
            num += 1

        print(f"buf4 = {buf4}")
        return num


obj = Solution()
print(obj.read(buf="abc", n=4))
print(obj.read(buf="abcde", n=4))

