# 624. Maximum Distance in Arrays

# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

# Return the maximum distance.



class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = float('-inf')
        max_val = arrays[0][-1]
        min_val = arrays[0][0]

        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][0] - max_val))
            result = max(result, abs(arrays[i][-1] - min_val))
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])

        return result