# Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) where x is an element from arr and y is an element from brr.


#User function Template for python3

import math
class Solution:
    
#Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code here
        for i in range(len(arr)):
            arr[i]=math.log(arr[i])/arr[i]
        for i in range(len(brr)):
            brr[i]=math.log(brr[i])/brr[i]
        arr.sort()
        brr.sort()
        cnt=0
        for i in range(len(arr)):
            idx=bisect.bisect_left(brr,arr[i])
            cnt+=idx
        return cnt


#{ 
# Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends