class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(counter.containsKey(nums[i])){
                return true;
            }else{
                counter.put(nums[i], 1);
            }
        }
        System.out.println(counter);

        return false;
    }
}