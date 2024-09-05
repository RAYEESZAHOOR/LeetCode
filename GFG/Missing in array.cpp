// Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. The array is a permutation of size n with one element missing. Return the missing element.

class Solution {
public:

    // Note that the size of the array is n-1
    int missingNumber(int n, vector<int>& arr) {

        // Your code goes here
        int x=0;
        for(int i=1;i<=n;i++) x^=i;
        for(int i=0;i<n-1;i++) x^=arr[i];
        return x;
    }
};
