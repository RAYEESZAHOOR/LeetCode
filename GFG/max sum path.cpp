// Max sum path in two arrays
// Difficulty: MediumAccuracy: 30.9%Submissions: 61K+Points: 4
// Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any array. You can switch from one array to another array only at the common elements.

// Note:  When we switch from one array to other,  we need to consider the common element only once in the result.


class Solution {
public:
    int maxPathSum(vector<int> &arr1, vector<int> &arr2) {
        int n1 = arr1.size() , n2 = arr2.size();
        vector<int> common;
        int prev_sum1 = 0 , prev_sum2 = 0;
        int ans = 0;
        int i = 0 , j = 0;
        while(i < n1 && j < n2){
            if(arr1[i] == arr2[j]){
                ans += arr1[i];
                ans = ans + max(prev_sum1 , prev_sum2);
                prev_sum1 = 0;
                prev_sum2 = 0;
                i++;
                j++;
            }
            else if(arr1[i] < arr2[j]){
                prev_sum1 += arr1[i];
                i++;
            }
            else{
                prev_sum2 += arr2[j];
                j++;
            }
        }
        while(i < n1){
            prev_sum1 += arr1[i];
            i++;
        }
        while(j < n2){
            prev_sum2 += arr2[j];
            j++;
        }
        ans += max(prev_sum1,prev_sum2);
        return ans;
    }
};