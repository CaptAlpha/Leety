class Solution {
public:
    void sortColors(vector<int>& nums) {
        int z, o, t;
        z = o = t = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i]==1){
                o++;
            }else if(nums[i]==2){
                t++;
            }else{
                z++;
            }
        }
        nums.clear();
        for(int i = 0; i < z; i++){
            nums.push_back(0);
        }
        for(int i = 0; i < o; i++){
            nums.push_back(1);
        }
        for(int i = 0; i < t; i++){
            nums.push_back(2);
        }
        
        
        
    }
};