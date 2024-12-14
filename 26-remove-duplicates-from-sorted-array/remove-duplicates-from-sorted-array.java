class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) return 0; // Handle edge cases

        int i = 0; // Pointer for the last unique element
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) { // When a new unique element is found
                i++; // Move the pointer for unique elements
                nums[i] = nums[j]; // Update the position with the new unique element
            }
        }

        return i + 1; // Return the number of unique elements
    }
}
