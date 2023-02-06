#coding=utf8

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

'''
s = 'aab'
p = 'c*a*b'
'''

class Solution(object):
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     if not (p and s):
    #         return False
    #     m = p[0]
    #     m_next = p[1] if len(p) > 1 else None
    #     char = s[0]
    #     match = False
    #     length = len(s)
    #
    #     if m == '.':
    #         match = True
    #         if length > 1:
    #             if m_next:
    #                 if m_next == '*':
    #                     return True
    #                 else:
    #                     return self.isMatch(s[1:], p[1:])
    #             else:
    #                 return False
    #         else:
    #             return True
    #     elif m == char:
    #         match == True
    #         if length > 1:
    #             pass
    #         else:
    #             pass
    #     else:
    #         if m_next:
    #             if m_next == '*':
    #                 return self.isMatch(s, p[2:])
    #             else:
    #                 return self.isMatch(s, p[1:])
    #         else:
    #             return False
    cache = {}
    def isMatch(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s , p)]

        if not p: # 如果p没了,但是还有s,返回Flase
            return not s

        if p[-1] == '*':
            if self.isMatch(s, p[:-2]): # '*' Matches zero
                self.cache[(s, p[:-2])] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p): # '*'' match many
                self.cache[(s, p)] = True
                return True

        if s and (s[-1] == p[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]): # 向左移动p
            self.cache[(s, p)] = True
            return True
        else:
            self.cache[(s, p)] = False
            return False

    def isMatch2(self, s, p):
        """
        dymatic programming 动态规划
        dp 保存各组match的记录
        例如 : s = 'aab', p = 'c*a*b'

                     a  a  b
               s  0  1  2  3
            p   --------------
              0 | 1  0  0  0 |
            c 1 | 0  0  0  0 |
            * 2 | 1  0  0  0 |
            a 3 | 0  1  0  0 |
            * 4 | 1  1  1  0 |
            b 5 | 0  0  0  1 |

        db[i+1][j+1]保存的是 s[:i]和p[:j]的结果
        判断db[i+1][j+1]的结果:
            if p[i] == '*':
                pass
            else:
                如果 db[i][j] == True
                如果 p[i] == '.' or p[i] == s[i]
                则: 真
        """
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        for i in dp:
            print(i)
        return dp[-1][-1]



if __name__ == '__main__':
    s = 'aabcacacaca'
    p = 'a.*'
    sol = Solution()
    result = sol.isMatch2(s, p)
    print(result)
