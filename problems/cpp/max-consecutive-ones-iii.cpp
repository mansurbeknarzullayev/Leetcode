class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int ans = 0, pos = 0, cnt = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            if(nums[i] == 0){
                cnt ++;
            }
            while(cnt > k){
                if(nums[pos] == 0){
                    cnt --;
                }
                pos ++;
            }
            ans = max(ans, i - pos + 1);
        }
        return ans;
    }
};