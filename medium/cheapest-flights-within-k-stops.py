from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adjList = [[] for _ in range(n)]
        for a, b, p in flights:
            adjList[a].append((b, p))
        minCost = [float("inf") for _ in range(n)]
        q = [(src, 0)]

        stops = 0
        # bfs
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                curNode, cost = q.pop(0)
                for neb, price in adjList[curNode]:
                    if cost + price > minCost[neb]:
                        continue
                    minCost[neb] = cost + price
                    q.append((neb, minCost[neb]))
            stops += 1

        return -1 if minCost[dst] == float("inf") else minCost[dst]


if __name__ == "__main__":
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print(Solution().findCheapestPrice(4, flights, 0, 3, 1))
