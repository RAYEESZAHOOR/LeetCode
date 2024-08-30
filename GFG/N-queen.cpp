// # N-Queen Problem
// # Difficulty: HardAccuracy: 35.43%Submissions: 78K+Points: 8
// # The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
// # Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].

// User function Template for C++
#include <vector>

class Solution {
public:
    // Check if placing a queen at (r, c) is valid
    bool check(const std::vector<std::vector<int>>& arr, int r, int c) {
        int n = arr.size();

        // Check column
        for (int i = 0; i < r; i++) {
            if (arr[i][c] == 1) return false;
        }

        // Check upper left diagonal
        for (int i = r, j = c; i >= 0 && j >= 0; i--, j--) {
            if (arr[i][j] == 1) return false;
        }

        // Check upper right diagonal
        for (int i = r, j = c; i >= 0 && j < n; i--, j++) {
            if (arr[i][j] == 1) return false;
        }

        return true;
    }

    // Backtracking function to find all solutions
    void get(int n, int r, std::vector<std::vector<int>>& arr, std::vector<std::vector<int>>& ans) {
        if (r >= n) {
            std::vector<int> temp;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (arr[i][j] == 1) {
                        temp.push_back(j+1);
                    }
                }
            }
            ans.push_back(temp);
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (check(arr, r, i)) {
                arr[r][i] = 1;
                get(n, r + 1, arr, ans);
                arr[r][i] = 0; // Backtrack
            }
        }
    }

    std::vector<std::vector<int>> nQueen(int n) {
        std::vector<std::vector<int>> ans;
        std::vector<std::vector<int>> arr(n, std::vector<int>(n, 0));
        get(n, 0, arr, ans);
        return ans;
    }
};

