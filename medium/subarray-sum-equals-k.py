from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {0: 1}
        count = 0
        prefsum = 0
        for num in nums:
            prefsum = prefsum + num
            if prefsum - k in mem:
                count += mem[prefsum - k]
            if prefsum not in mem:
                mem[prefsum] = 1
            else:
                mem[prefsum] += 1

        return count
