"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def dfs(node):
            if not node:
                return 0
            hashmap[node] = neighbors
            return dfs(neighbors)
        dfs(node)
        self.all_nodes = [n for pair in d.items() for n in pair]
        return self.all_nodes
        