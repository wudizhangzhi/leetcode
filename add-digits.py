# coding=utf8
from deco import runningtime
'''
 Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

import operator
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num<10 else self.addDigits(reduce(lambda x,y:int(x)+int(y) ,list(str(num))))

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        else:
            return (num-1)%9 +1



if __name__ == '__main__':
    import time
    import random
    sol = Solution()
    start = time.time()
    print sol.addDigits(random.randint(1000,9999))
    print time.time()-start
