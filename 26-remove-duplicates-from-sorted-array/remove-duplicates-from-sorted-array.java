class Solution {
    public int removeDuplicates(int[] nums) {
        TreeSet<Integer> set = new TreeSet<>();
        for(int i: nums){
            set.add(i);
        }
        // Convert the TreeSet to an Integer array
        Integer[] arr = set.toArray(new Integer[0]);

        // Copy the unique elements back to the original array
        for (int i = 0; i < arr.length; i++) {
            nums[i] = arr[i];
        }

        // Return the size of the TreeSet (number of unique elements)
        return set.size();
    }
}