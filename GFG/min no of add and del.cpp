
// Minimum number of deletions and insertions
// Difficulty: Medium

// Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

class Solution{
        

    public:
    int arr[1001][1001];
    int f(string &str1, string &str2, int i, int j){
        if(i<0) return j+1;
        if(j<0) return i+1;
        
        if(arr[i][j]!=-1) return arr[i][j];
        
        if(str1[i]==str2[j]){
            return arr[i][j]=f(str1,str2,i-1,j-1);
        }
        else{
            int tk = 1+f(str1,str2,i-1,j);
            int ntk = 1+f(str1,str2,i,j-1);
            return arr[i][j]=min(tk,ntk);
        }
    }
    int minOperations(string str1, string str2) 
    { 
        // Your code goes here
        memset(arr,-1,sizeof(arr));
        return f(str1,str2,str1.length()-1,str2.length()-1);
    } 
};