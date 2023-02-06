from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5)
    print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)
    print(Solution().maxProfit([2, 4, 1]) == 2)
