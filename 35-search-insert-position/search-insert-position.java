class Solution {
    public int binSearch(int[] arr, int left, int right, int target) {
        if (left > right) {
            return left; // Return the position to insert if not found
        }
        int mid = left + (right - left) / 2; // Calculate mid to avoid overflow

        if (arr[mid] == target) {
            return mid; // Target found
        }
        if (arr[mid] > target) {
            return binSearch(arr, left, mid - 1, target); // Search in the left half
        } else {
            return binSearch(arr, mid + 1, right, target); // Search in the right half
        }
    }

    public int searchInsert(int[] nums, int target) {
        return binSearch(nums, 0, nums.length - 1, target);
    }
}
