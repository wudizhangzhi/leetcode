from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,1,1,9]
        mem = [0] * len(nums)  # 存储最大值
        mem[0] = nums[0]
        for i in range(1, len(nums)):
            include = nums[i] + mem[i - 2] if i - 2 >= 0 else nums[i]
            exclude = mem[i - 1]
            mem[i] = max(include, exclude)
        return mem[-1]


if __name__ == "__main__":
    nums = [2, 1, 1, 9]
    print(Solution().rob(nums))
