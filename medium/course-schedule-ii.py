from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        adjList = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[a].append(b)
            degrees[b] += 1

        bfs = [i for i in range(numCourses) if degrees[i] == 0]
        for i in bfs:
            for node in adjList[i]:
                print(i, node)
                degrees[node] -= 1
                if degrees[node] == 0:
                    bfs.append(node)
        return bfs[::-1] if len(bfs) == numCourses else []


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(numCourses, prerequisites))
