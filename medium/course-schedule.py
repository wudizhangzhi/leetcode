"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            adjList[a].append(b)
            degree[b] += 1  # b点入度加1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for n in bfs:
            for v in adjList[n]:
                degree[v] -= 1
                if degree[v] == 0:
                    bfs.append(v)
        # 入度为0的点就是不在有环图中的点
        return len(bfs) == numCourses


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0], [0, 1]]) == False)
    print(Solution().canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) == True)
