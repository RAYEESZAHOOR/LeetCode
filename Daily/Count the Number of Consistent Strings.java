// You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

// Return the number of consistent strings in the array words.



class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int arr[]=new int[26];
        for(char i:allowed.toCharArray()){
            arr[i-'a']=1;
        }
        int count=0;
        for(String k:words){
            count+=findConsistentString(arr,k);
        }
        return count;
    }
    public static int findConsistentString(int arr[],String k){
        int flag=1;
        for(int i=0;i<k.length();i++){
            if(arr[k.charAt(i)-'a']==0){
                flag=0;
                break;
            }
        }
        return flag;
    }
}