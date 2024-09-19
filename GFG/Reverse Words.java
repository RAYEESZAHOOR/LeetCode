
// Given a String str, reverse the string without reversing its individual words. Words are separated by dots.

// Note: The last character has not been '.'. 


class Solution {
    // Function to reverse words in a given string.
    String reverseWords(String str) {
        // code here
        if (str.length() == 0)
            return "";
        int n = str.length();
        String sol = "";
        String temp = "";
        int i = n - 1;
        while (i >= 0) {
            char k = str.charAt(i);
            if (k != '.') {
                temp = k + temp;
            } else {
                sol = sol + temp + ".";
                temp = "";
            }
            i--;
        }
        sol = sol + temp;
        return sol;
    }
}