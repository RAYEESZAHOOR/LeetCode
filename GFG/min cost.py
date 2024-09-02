# Minimum Cost Path
# Difficulty: HardAccuracy: 26.99%Submissions: 93K+Points: 8
# Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
# From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

import heapq

class Solution:
    
    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.
    def minimumCostPath(self, grid):
        heap, vis = [], set()
        self.n, self.m = len(grid), len(grid[0])
        dist = [[float("inf")] * self.m for _ in range(self.n)]
        dist[0][0] = grid[0][0]
        
        def dijkstra():
            heapq.heappush(heap, (dist[0][0], 0, 0))
            while heap:
                node, i, j = heapq.heappop(heap)
                for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nx, ny = x + i, y + j
                    if 0 <= nx < self.n and 0 <= ny < self.m:
                        if dist[nx][ny] > grid[nx][ny] + node:
                            dist[nx][ny] = grid[nx][ny] + node
                            heapq.heappush(heap, (dist[nx][ny], nx, ny))
        
        dijkstra()
        return dist[self.n - 1][self.m - 1]





#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends