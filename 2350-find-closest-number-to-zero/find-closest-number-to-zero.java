class Solution {
    public int findClosestNumber(int[] nums) {
        int val = -1;
        int delta = Integer.MAX_VALUE;
        for(int num: nums){
            if (num>=0){
                if(delta>=num){
                    delta=num;
                    val = num;
                }
            }else{
                if(delta>-1*num){
                    delta=-1*num;
                    val = num;
                }
            }
        }
        return val;
    }
}