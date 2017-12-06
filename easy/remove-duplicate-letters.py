# coding=utf8
from deco import runningtime

'''
Given a string which contains only lowercase letters, remove duplicate letters so
that every letter appear once and only once. You must make sure your result is
the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            print c, s, suffix
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''


if __name__ == '__main__':
    Input = "cbacdcbc"

    sol = Solution()
    # Output = sol.findDisappearedNumbers(Input)
    Output = sol.removeDuplicateLetters(Input)
    print 'Output:%s' % Output
