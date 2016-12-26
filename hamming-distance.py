# coding=utf8
from deco import runningtime

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''
class Solution(object):
    @runningtime
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum([1 if a!=b else 0 for a,b in zip(bin(x).replace('0b','').zfill(32), bin(y).replace('0b','').zfill(32))])

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

if __name__ == '__main__':
    sol = Solution()
    x = 109
    y = 345
    print sol.hammingDistance(x, y)
