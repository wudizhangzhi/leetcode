# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        clones = {}

        def dfs(node):
            if node.val in clones:
                return clones[node.val]
            copy = Node(node.val, [])
            clones[node.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else node


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    print(Solution().cloneGraph())
