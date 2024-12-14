class Solution {
    public int binSearch(int[] arr, int target, int left, int right) {
        if (left > right) {
            return -1; // Base case: target not found
        }

        int mid = left + (right - left) / 2; // Avoid potential overflow
        if (arr[mid] == target) {
            return mid; // Target found
        }

        if (arr[mid] < target) {
            return binSearch(arr, target, mid + 1, right); // Search in the right half
        } else {
            return binSearch(arr, target, left, mid - 1); // Search in the left half
        }
    }

    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1; // Handle edge case
        }
        return binSearch(nums, target, 0, nums.length - 1);
    }
}
