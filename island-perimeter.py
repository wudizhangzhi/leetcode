#coding=utf8
import sys
sys.path.append('..')
from tools.kuaipai import runningtime
'''
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
 One cell is a square with side length 1. The grid is rectangular,
 width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
class Solution(object):
    @runningtime
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        思路:计算周长，
            分别计算横向的长度，和纵向的长度
            例如，计算横向的长度，如果列表偏移一格后对比原位置数值不想等，说明该位置是陆地，
                因为横向长度有两面，上面有了1，下面也肯定有1，所以横向长度=一边数值×2
        """
        import operator
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))


class Solution2(object):
    @runningtime
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        一个格子周长是4
        上面是陆地 -1
        下面是陆地 -1
        左边是陆地 -1
        右边是陆地 -1

        所以，每个格子的周长是0
        上面是海 +1
        下面是海 +1
        。
        。
        """
        def water_around(y, x):
            return (y==0 or grid[y-1][x] == 0) +\
                (y==len(grid)-1 or grid[y+1][x] == 0) +\
                (x==0 or grid[y][x-1] == 0) +\
                (x==len(grid[y])-1 or grid[y][x+1] == 0)


        return sum([water_around(y,x) for y, row in enumerate(grid) for x, cell in enumerate(row) if grid[y][x]])



if __name__ == '__main__':
    test = [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    sol = Solution()
    print sol.islandPerimeter(test)
    sol2 = Solution2()
    print sol2.islandPerimeter(test)
