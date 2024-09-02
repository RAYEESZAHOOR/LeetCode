// 1894. Find the Student that Will Replace the Chalk
// Medium
// Topics
// Companies
// Hint
// There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

// You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

// Return the index of the student that will replace the chalk pieces.

class Solution {
public:
    static int chalkReplacer(vector<int>& chalk, int k) {
        const int n=chalk.size();
        vector<long long> sum(n, chalk[0]);// prefix sum 0-indexed 
        for(int i=1; i<n; i++){
            sum[i]=sum[i-1]+chalk[i];
        //    cout<<i<<"->"<<sum[i]<<endl;
        }
        k%=sum[n-1];
    //    cout<<"k="<<k<<endl;

        return upper_bound(sum.begin(), sum.end(), k)-sum.begin();
    }
};




auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();