class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
         map<int,int>m;

        vector<int>v;

        

        for(int i=0;i<nums.size();i++){

            m[nums[i]]++;

            if(m[nums[i]]>1){

                continue;

            }

            v.push_back(nums[i]);

        }

        nums=v;

        return v.size();
    }
};