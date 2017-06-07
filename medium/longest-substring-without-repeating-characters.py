#coding
'''
Given a string, find the length of the longest
substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
 "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        longest = 0
        usedChar = {}
        start = 0
        for i in xrange(length):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)
            usedChar[s[i]] = i
        return longest


if __name__ == "__main__":
    s = 'pwwkew'
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
