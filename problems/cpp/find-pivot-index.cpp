class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int sum = 0, sum_l = 0;
        for(int i = 0; i < n; i++){
            sum += nums[i];
        }
        for(int i = 0; i < n; i++){
            sum -= nums[i];
            if(sum_l == sum){
                return i;
            }
            sum_l += nums[i];
        }
        return -1;
    }
};