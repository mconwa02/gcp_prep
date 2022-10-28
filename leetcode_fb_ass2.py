from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sq_nums = []
        for i in range(n):
            sq_nums.append(nums[i] * nums[i])
        return sorted(sq_nums)


nums = [-4, -1, 0, 3, 10]
obj = Solution()
print(obj.sortedSquares(nums=nums))


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ''
        for i in range(len(order)):
            if order[i] in s:
                output += order[i]
        for i in range(len(s)):
            if s[i] not in output:
                output += s[i]
        return output


obj = Solution()
print(obj.customSortString('cba', 'abcd'))
print(obj.customSortString('cbafg', 'abcd'))
print(obj.customSortString('kqep', 'pekeq'))

