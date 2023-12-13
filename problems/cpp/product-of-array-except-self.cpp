class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>suff = nums;
        vector<int>pref = nums;
        for(int i = 1; i < n; i++){
            pref[i] *= pref[i - 1];
        }
        for(int i = n - 2; i >= 0; i--){
            suff[i] *= suff[i + 1];
        }
        for(int i = 0; i < n; i++){
            nums[i] = 1;
            if(i > 0){
                nums[i] *= pref[i - 1];
            }
            if(i + 1 < n){
                nums[i] *= suff[i + 1];
            }
        }
        return nums;
    }
};