# -*- coding:utf8 -*-


"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        s = s[::-1]
        result = 0
        for i in xrange(length):
            result += (ord(s[i]) - 64)*(26**i)
        return result

    def titleToNumber2(self, s):
        return reduce(lambda x,y: x*26 + y , map(lambda x: ord(x) - ord('A') + 1, s))


if __name__ == '__main__':
    s = 'AB'
    sol = Solution()
    result = sol.titleToNumber(s)
    print(result)
    result2 = sol.titleToNumber2(s)
    print(result2)
