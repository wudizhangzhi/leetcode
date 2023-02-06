# coding=utf8
from deco import runningtime
'''
 Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''

class Solution(object):
    @runningtime
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sl = list(s)
        tl = list(t)
        for i in sl:
            tl.remove(i)
        return tl[0]

    @runningtime
    def findTheDifference2(self, s, t):
        """
        太慢了
        :type s: str
        :type t: str
        :rtype: str
        """
        # s = sorted(list(s))
        # t = sorted(list(t))
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in xrange(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

    @runningtime
    def findTheDifference3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import operator
        return chr(reduce(operator.xor, map(ord, s + t)))

    @runningtime
    def findTheDifference4(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        快的方法
        """
        anns = 0
        for i in (s+t):
            anns ^= ord(i)
        return chr(anns)


    @runningtime
    def findTheDifference5(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        使用zip
        """
        s ,t = sorted(s), sorted(t)
        return t[-1] if s==t[:-1] else [x[1] for x in zip(s,t) if x[0]!=x[1]][0]


if __name__ == '__main__':
    import random
    import string
    lower = string.letters[:26]
    s = ''.join([random.choice(lower) for i in xrange(random.randint(10,100))])
    # print s
    sl = list(s)
    diff = random.choice(lower)
    # print 'diff:%s' % diff
    index = random.randint(0,len(s))
    sl.insert(index, diff)
    random.shuffle(sl)
    t = ''.join(sl)
    print '数据长度:%s , 插入位置:%s' % (len(s), index)

    sol = Solution()
    print sol.findTheDifference(s, t) == diff
    print sol.findTheDifference2(s, t) == diff
    print sol.findTheDifference3(s, t) == diff
    print sol.findTheDifference4(s, t) == diff
    print sol.findTheDifference5(s, t) == diff