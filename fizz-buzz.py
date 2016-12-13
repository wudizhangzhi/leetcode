#coding=utf8

'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [Solution.handler(i) for i in xrange(1, n+1)]

    @classmethod
    def handler(cls, num):
        if num%3==0 and num%5==0:
            return 'FizzBuzz'
        elif num%3==0 and num%5!=0:
            return 'Fizz'
        elif num%3!=0 and num%5==0:
            return 'Buzz'
        else:
            return str(num)

class Solution2(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i)  for i in xrange(1, n+1)]


if __name__ == '__main__':
    sol = Solution()
    print sol.fizzBuzz(20)
    sol2 = Solution2()
    print sol2.fizzBuzz(20)
