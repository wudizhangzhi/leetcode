"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1: int, s2):
            return str(s1) + str(s2) < str(s2) + str(s1)

        leng = len(nums)
        for i in range(leng):
            for j in range(i, leng):
                if compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        ans = ""
        for num in nums:
            ans += str(num)
        return ans


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
