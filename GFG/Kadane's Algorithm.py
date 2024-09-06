# Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ans, curr = arr[0], 0
        for item in arr:
            curr += item
            ans = max(curr, ans)
            curr = max(curr, 0)
        
        return ans