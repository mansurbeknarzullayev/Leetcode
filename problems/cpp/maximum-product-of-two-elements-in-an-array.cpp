class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int len = nums.size();
        for(int i = 0; i < len; i++){
            nums[i] --;
        }
        sort(nums.begin(), nums.end());
        return max(nums[0] * nums[1], nums[len - 1] * nums[len - 2]);
    }
};