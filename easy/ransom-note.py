# coding=utf8
from deco import runningtime

'''
 Given an arbitrary ransom note string and another string containing letters
  from all the magazines, write a function that will return true if the ransom
  note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

if __name__ == '__main__':
    ransomNote = 'aa'
    magazine = 'ab'
    sol = Solution()
    # Output = sol.findDisappearedNumbers(Input)
    Output = sol.canConstruct(ransomNote, magazine)
    print 'Output:%s' % Output
