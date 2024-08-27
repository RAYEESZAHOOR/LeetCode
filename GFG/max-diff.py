# Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left smaller element and the nearest right smaller element of every element in array arr. If for any component of the arr, the nearest smaller element doesn't exist then consider it as 0.

class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        # Initialize left and right smaller arrays
        ls = [0] * n
        rs = [0] * n
        
        # Stack to find left smaller
        stack = []
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            ls[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        # Clear the stack for right smaller processing
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            rs[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))
        
        return max_diff

        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends