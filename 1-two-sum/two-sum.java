class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if the complement already exists in the map
            if (hashMap.containsKey(complement)) {
                return new int[] { hashMap.get(complement), i };
            }
            
            
            // Store the current number and its index in the map
            hashMap.put(nums[i], i);
        }
        return new int[] { 0, 0 };
 
    }
}