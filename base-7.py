# coding=utf8
from deco import runningtime
'''
Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        col = 0

        _num = abs(num)*7

        while _num >= 7:
            n = -1
            _num = (_num - col*7**n)/7
            col = _num%7
            result.append(str(int(col)))
            n += 1

        if num < 0:
            result.append('-')

        return ''.join(result[::-1])


    def convertToBase72(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertToBase72(-num)
        if abs(num) < 7:
            return str(num)
        return self.convertToBase72(num//7) + str(num%7)


if __name__ == '__main__':
    Input = -100
    sol = Solution()
    output = sol.convertToBase7(Input)
    print output
    output = sol.convertToBase72(Input)
    print output
