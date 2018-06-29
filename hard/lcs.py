#coding=utf8
'''
求取最长公共子序列问题(longest-common-subsquence problem)
'''
import numpy as np
import random

def export_x_y(num_x, num_y):
    '''
    生成2个随机的序列
    '''
    letters = 'ABCD'
    x = [random.choice(list(letters)) for _ in range(num_x)]
    y = [random.choice(list(letters)) for _ in range(num_y)]
    return x, y


def lcs_length(x, y):
    length_x = len(x)
    length_y = len(y)
    c = np.zeros((length_x, length_y))
    b = c.copy()
    for i in range(1, length_x):
        for j in range(1, length_y):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = ord('\\')
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = ord('|')
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = ord('-')
    return c, b


def print_lcs(b, x, i, j):
    result = []
    def _print_lcs(b, x, i, j, result):
        if i ==0 or j==0:
            return
        if b[i][j] == ord('\\'):
            result.append(x[i])
            _print_lcs(b, x, i-1, j-1, result)
        elif b[i][j] == ord('|'):
            _print_lcs(b, x, i-1, j, result)
        elif b[i][j] == ord('-'):
            _print_lcs(b, x, i, j-1, result)
    _print_lcs(b, x, i, j, result)
    return ''.join(result[::-1])


def print_lcs_v2(c, x, i, j):
    result = []
    def _print_lcs_v2(c, x, i, j, result):
        if i==0 or j==0:
            return
        if c[i][j] == c[i-1][j-1] + 1:
            result.append(x[i])
            _print_lcs_v2(c, x, i-1, j-1, result)
        elif c[i][j] == c[i-1][j]:
            _print_lcs_v2(c, x, i-1, j, result)
        elif c[i][j] == c[i][j-1]:
            _print_lcs_v2(c, x, i, j-1, result)
    _print_lcs_v2(c, x, i, j, result)
    return ''.join(result[::-1])


def test(count):
    fail = 0
    success = 0
    for i in range(count):
        x, y = export_x_y(11, 10)
        c, b = lcs_length(x, y)
        lcs = print_lcs(b, x, len(x)-1, len(y)-1)
        lcs2 = print_lcs_v2(c, x, len(x)-1, len(y)-1)
        if not c[-1][-1] == len(lcs) == len(lcs2):
            fail +=1
        else:
            success +=1
    print('共验算: %s次' % count)
    print('成功率:%0.2f%%' % (success*100.0/count))


if __name__ == '__main__':
    x, y = export_x_y(11, 10)
    print(x)
    print(y)
    c, b = lcs_length(x, y)
    print('lcs_length: %s' % c[-1][-1])
    lcs = print_lcs(b, x, len(x)-1, len(y)-1)
    print(lcs)
    lcs = print_lcs_v2(c, x, len(x)-1, len(y)-1)
    print(lcs)

    test(1000)
