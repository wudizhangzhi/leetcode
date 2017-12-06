#coding=utf8

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"


A palindrome is a string which reads the same in both directions. For example, ”aba” is a palindome, ”abc” is not.
'''

class Solution(object):
    result = '' 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < len(self.result): 
            return self.result
        if self.is_palindome(s):
            if len(s) > len(self.result):
                self.result = s 
            return s 
        else:
            left = self.longestPalindrome(s[1:])
            right = self.longestPalindrome(s[:-1])
            return max(left, right, key=lambda x: len(x))

    def is_palindome(self, s):
        return s == s[::-1]
    
    def longestPalindrome2(self, s):
        if len(s) == 0:
            return None
        start = 0
        maxLen = 1
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i-maxLen-1: i+1] == s[i-maxLen-1: i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2
            if i - maxLen >= 0 and s[i-maxLen: i+1] == s[i-maxLen: i+1][::-1]:
                start = i-maxLen
                maxLen += 1
        return s[start: start+maxLen]

if __name__ == '__main__':
    inputs = "babaddtattarrattatddetartrateedredividerb" 
    sol = Solution()
    output = sol.longestPalindrome2(inputs) 
    print(output)
    print(sol.is_palindome(output))
