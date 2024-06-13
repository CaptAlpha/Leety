class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(hashmap.containsKey(nums[i])){
                return true;
            }
            hashmap.put(nums[i], 1);
        }
        return false;
    }
}