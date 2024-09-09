
// Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.
class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(ArrayList<Integer> arr) {
        // code here
        int i;
        int count0 = 0;
        int count1 = 0;
        int count2 = 0;
        
        for(i = 0;i<arr.size();i++){
            if(arr.get(i)==0){
                count0++;
            }
            if(arr.get(i)==1){
                count1++;
            }
            if(arr.get(i)==2){
                count2++;
            }
        }
        arr.clear();
        int index = 0;
        for(i = 0;i<count0;i++){
            arr.add(index,0);
            index++;
        }
        for(i = 0;i<count1;i++){
            arr.add(index,1);
            index++;
        }
        for(i = 0;i<count2;i++){
            arr.add(index,2);
            index++;
        }
    }
}