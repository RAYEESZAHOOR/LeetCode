# 0 - 1 Knapsack Problem
# You are given weights and values of items, and put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val and wt which represent values and weights associated with items respectively. Also given an integer W which represents knapsack capacity, find out the maximum sum values subset of val[] such that the sum of the weights of the corresponding subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        mat=[[0 for j in range(W+1)] for i in range(len(val)+1)]
        for i in range(1,len(val)+1):
            for j in range(1,W+1):
                if wt[i-1] <= j:
                    mat[i][j] = max(mat[i-1][j], mat[i-1][j-wt[i-1]] + val[i-1])
                else:
                    mat[i][j] = mat[i-1][j]
        return mat[-1][-1]

#{ 
# Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends