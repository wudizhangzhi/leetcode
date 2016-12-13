# coding=utf8
import sys
sys.path.append('..')
from tools.kuaipai import runningtime
'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


class Solution(object):
    @runningtime
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        python貌似使用64bit计算
        """
        MAX = 0x7FFFFFFF # 32bit 最大值
        mask = 0xFFFFFFFF  # 32bit
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

            '''
            二进制加法：
            例如: a = 5 = 0b101
                 b = 3 =  0b11
                 a + b :
                         0b101
                        + 0b11
                        -------
                       =0b1000
            加法的过程：每一位比较，都为1则进1

            (a ^ b) & mask：a 和 b的异或集合， 二进制中不同的取1， 意义：完成那些不需要进位的
            a&b : a 和 b 的并集合，二进制中相同的取1， 意义：得到进位
            (a&b)<<1： 意义：向左进1位，赋值给b， 再与a比较找出需要进位和不需要进位的，
                        当b=0即 a，b没有都为1的位时候，a就是a+b的值
            #TODO
                else ~(a & mask)不是非常理解
            '''
        return a if a<=MAX else ~(a & mask)


if __name__ == '__main__':
    import random
    # a = random.randint(1000000000000,9999999999999999)
    # b = random.randint(33333333,77777777)
    a = -1
    b = -1
    sol = Solution()
    result = sol.getSum(a,b)
    print '%s + %s = %s' % (a, b, result)
    print a+b==result
