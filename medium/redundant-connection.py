from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        degrees = defaultdict(int)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            degrees[a] += 1
            degrees[b] += 1

        zeroDegrees = [i for i in range(1, len(edges) + 1) if degrees[i] == 1]
        for n in zeroDegrees:
            seen = set()
            for neighbour in adj[n]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                degrees[neighbour] -= 1
                if degrees[neighbour] == 1:
                    zeroDegrees.append(neighbour)
        for edge in edges[::-1]:
            if edge[0] not in zeroDegrees and edge[1] not in zeroDegrees:
                return edge
        return []


if __name__ == "__main__":
    edges = [
        [16, 25],
        [7, 9],
        [3, 24],
        [10, 20],
        [15, 24],
        [2, 8],
        [19, 21],
        [2, 15],
        [13, 20],
        [5, 21],
        [7, 11],
        [6, 23],
        [7, 16],
        [1, 8],
        [17, 20],
        [4, 19],
        [11, 22],
        [5, 11],
        [1, 16],
        [14, 20],
        [1, 4],
        [22, 23],
        [12, 20],
        [15, 18],
        [12, 16],
    ]
    print(Solution().findRedundantConnection(edges))
