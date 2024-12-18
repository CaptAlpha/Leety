import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums); // Step 1: Sort the array to use two pointers efficiently

        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicates for the first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int target = -nums[i]; // Step 2: Find two numbers that sum to -nums[i]
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Skip duplicates for the second and third elements
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    // Move both pointers inward after processing a valid triplet
                    left++;
                    right--;
                } else if (sum < target) {
                    // If sum is less than the target, move the left pointer to increase the sum
                    left++;
                } else {
                    // If sum is greater than the target, move the right pointer to decrease the sum
                    right--;
                }
            }
        }
        return result;
    }
}
