class Solution {
public:
    void sortColors(vector<int>& nums) {
        int a, b, c;
        a = b = c = 0;

             for (auto i : nums) {
            if (i == 0) {
                a++;
            } else if (i == 1) {
                b++;
            } else {
                c++;
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            if (i < a) {
                nums[i] = 0;
            } else if (i < a + b) {
                nums[i] = 1;
            } else {
                nums[i] = 2;
            }
        }
    }
};