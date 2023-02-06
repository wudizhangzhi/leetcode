from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if not edges:
            return True
        visisted = set()

        adjList = [[] for _ in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        # LIFO
        stack = [source]
        while stack:
            node = stack.pop(-1)
            visisted.add(node)
            for n in adjList[node]:
                if n == destination:
                    return True
                if n not in visisted:
                    stack.append(n)

        return False


if __name__ == "__main__":
    print(
        Solution().validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False
    )
