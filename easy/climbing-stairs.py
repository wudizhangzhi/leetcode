"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        第i个阶梯的步数 = 1次以内能达到第i阶梯的步数的和
        """
        if n < 3:
            return n
        dp = [0] * (n + 1)  # considering zero steps we need n+1 places
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == "__main__":
    print(Solution().climbStairs(44))
