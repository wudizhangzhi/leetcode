#coding=utf8
import sys
sys.path.append('..')
from tools.kuaipai import runningtime
'''
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
 The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game.
 Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game:
no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
'''

class Solution(object):
    @runningtime
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        绝对不会赢的情况：个数是4的倍数
        """
        return bool(n % 4)

class Solution2(object):
    @runningtime
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        因为4 的二进制是 100
        3的二进制是11
        只要是4的倍数的二进制最后2位都是00
        所以4的倍数与3的并集都是0
        """
        return bool(n & 3)


if __name__ == '__main__':
    sol = Solution()
    print sol.canWinNim(80)
    sol2 = Solution2()
    print sol2.canWinNim(80)
