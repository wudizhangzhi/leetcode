"""
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low, high, ans = 1, x, 0
        while low <= high:
            mid = (low + high + 1) // 2
            if x / mid == mid:
                return mid
            elif x / mid < mid:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans


if __name__ == "__main__":
    print(Solution().mySqrt(4) == 2)
    print(Solution().mySqrt(8) == 2)
    print(Solution().mySqrt(8192))
