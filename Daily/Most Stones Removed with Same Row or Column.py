# Most Stones Removed with Same Row or Column

# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

class Solution:
    def dfs(self, node, adj, visited):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                self.dfs(neighbor, adj, visited)
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]
        
        # Build the graph
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = set()
        numComponents = 0

        # Find the number of connected components
        for i in range(n):
            if i not in visited:
                self.dfs(i, adj, visited)
                numComponents += 1

        return n - numComponents