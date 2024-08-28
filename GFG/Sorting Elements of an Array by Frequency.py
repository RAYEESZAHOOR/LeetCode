# Given an array of integers arr, sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.

from collections import Counter

class Solution:
    def sortByFreq(self, arr):
        # Step 1: Count the frequency of each element
        freq = Counter(arr)
        
        # Step 2: Sort elements based on frequency (descending) and value (ascending)
        sorted_elements = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        # Step 3: Build the result list based on sorted elements
        result = []
        for element in sorted_elements:
            result.extend([element] * freq[element])
        
        return result