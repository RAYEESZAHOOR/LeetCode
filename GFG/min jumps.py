# Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
# Note:  Return -1 if you can't reach the end of the array.

class Solution {
    static int minJumps(int[] arr) {
        if (arr[0] == 0) {
            return -1;
        }
        
        int jump = 1;
        int pos = 0;
        while (pos + arr[pos] < arr.length - 1) {
            int max = 0;
            int tpos = pos;
            for (int i = pos + 1; i <= pos + arr[pos]; i++) {
                if (i > arr.length) {
                    break;
                }
                if (max < i + arr[i]) {
                    max = i + arr[i];
                    tpos = i;
                }
            }
            if (pos == tpos) {
                return -1;
            } else {
                pos = tpos;
                jump += 1;
            }
        }
        return jump;
    }
}