#coding=utf8
#coding=utf8


'''
分治  快速排序
'''
import time

def runningtime(func):
    '''
    显示运行时间
    '''
    def wraper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print '运行时间:%s' % (time.time() - start)
        return ret
    return wraper
