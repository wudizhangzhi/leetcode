# coding = utf8
"""
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.



Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.



Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.


      """


class Solution(object):
    # def thirdMax(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     formated = sorted(list(set(nums)), reverse=True)
    #     return formated[2] if len(formated) >=3 else formated[0]

    def thridMax(self, nums):
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        for num in nums:
            if num > first:
                second, third = first, second
                first = num
            elif first > num > second:
                second, third = num, second
            elif second > num > third:
                third = num
        if third == float("-inf"):
            return first
        return third


if __name__ == "__main__":
    inputs = ""
    sol = Solution()
    print(sol.thridMax([3, 2, 1]))
    print(sol.thridMax([1, 2]))
    print(sol.thridMax([2, 2, 3, 1]))
