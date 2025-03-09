class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i : nums) {
           int count = hashMap.getOrDefault(i, 0) + 1;

            // If the count exceeds nums.length / 2, return the element
            if (count > nums.length / 2) {
                return i;
            }

            // Update the count in the HashMap
            hashMap.put(i, count);
        }
        return -1;
    }
}