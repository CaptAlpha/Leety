class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length-1;
        while(numbers[left]+numbers[right]!=target){
            // If the sum of left and right is greater
            if(numbers[left]+numbers[right]>target){
                right-=1;
            }
            //If the sum of left and right is smaller
            else{
                left+=1;
            }
        }
        int[] ans = {left+1, right+1};
        return ans;
    }
}