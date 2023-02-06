from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = defaultdict(set)
        for i in range(len(equations)):
            adj[equations[i][0]].add((equations[i][1], values[i]))
            adj[equations[i][1]].add((equations[i][0], 1.0 / values[i]))

        res = []

        def dfs(node: str, target: str, value: int):
            if node == target:
                return value
            for neighbor, val in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, target, value * val)
                    if result != -1:
                        return result
                    # visited.remove(neighbor)
            return -1

        for start, end in queries:
            visited = set()
            if start not in adj or end not in adj:
                res.append(-1)
                continue
            res.append(dfs(start, end, 1))

        return res


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    print(Solution().calcEquation(equations, values, queries))
