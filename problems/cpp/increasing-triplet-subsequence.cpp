class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int min1, min2;
        bool f1 = false, f2 = false, f3 = false;
        for(int i = 0; i < nums.size(); i++){
            if(f2 && nums[i] > min2){
                f3 = true;
            }
            if(f1 && nums[i] > min1){
                if(f2){
                    min2 = min(min2, nums[i]);
                }
                else{
                    min2 = nums[i];
                }
                f2 = true;
            }
            if(f1){
                min1 = min(min1, nums[i]);
            }
            else{
                min1 = nums[i];
            }
            f1 = true;
        }
        return f3;
    }
};