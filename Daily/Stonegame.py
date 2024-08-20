# 1140. Stone Game II
# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
        
        return dp[0][1]