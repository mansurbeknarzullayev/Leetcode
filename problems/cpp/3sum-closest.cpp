class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int ans = 100000;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                int pos = lower_bound(nums.begin(), nums.end(), target - nums[i] - nums[j]) - nums.begin();
                for(int k = -3; k < 3; k++){
                    int p = pos + k;
                    if(0 <= p && p < n && p != i && p != j && abs(ans - target) > abs(nums[i] + nums[j] + nums[p] - target)){
                        ans = nums[i] + nums[j] + nums[p];
                    }
                }
            }
        }
        return ans;
    }
};