import java.util.ArrayList;
import java.util.List;

class Solution {
    public int subsetXORSum(int[] nums) {
        List<List<Integer>> subsets = generateSubarrays(nums);
        int totalXORSum = 0;

        for (List<Integer> subset : subsets) {
            totalXORSum += xorSum(subset);
        }

        return totalXORSum;
    }

    private int xorSum(List<Integer> arr) {
        int s = 0;
        for (int i : arr) {
            s ^= i;
        }
        return s;
    }

    private List<List<Integer>> generateSubarrays(int[] arr) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        generate(0, ans, ds, arr);
        return ans;
    }

    private void generate(int index, List<List<Integer>> ans, List<Integer> ds, int[] arr) {
        if (index == arr.length) {
            ans.add(new ArrayList<>(ds));
            return;
        }
        ds.add(arr[index]);
        generate(index + 1, ans, ds, arr);
        ds.remove(ds.size() - 1);
        generate(index + 1, ans, ds, arr);
    }
}
