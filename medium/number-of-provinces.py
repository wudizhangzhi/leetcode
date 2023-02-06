from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = set()
        ans = 0

        def dfs(n):
            visited.add(n)
            for neighbour in adj[n]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans


if __name__ == "__main__":
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(Solution().findCircleNum(isConnected))
