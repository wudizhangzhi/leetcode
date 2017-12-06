# coding=utf8
from deco import runningtime
'''
Given a List of words, return the words that can be typed using
 letters of alphabet on only one row's of American keyboard like the image below.

 Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
        result = []
        match = ''
        for word in words:
            word_lower = word.lower()
            for row in keyboard:
                if word_lower[0] in row:
                    match = row
                    break
            success = True
            for char in word_lower:
                if char not in match:
                    success = False
                    break
            if success:
                result.append(word)
        return result

    def findWords2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        运用集合的思想
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        result = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                result.append(word)
        return result

    def findWords3(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        运用正则
        """
        import re
        return filter(re.compile(r'(?i)^([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$', ).match, words)

if __name__ == '__main__':
    Input = ["Hello", "Alaska", "Dad", "Peace"]
    sol = Solution()
    output = sol.findWords2(Input)
    print output
    output = sol.findWords3(Input)
    print output
