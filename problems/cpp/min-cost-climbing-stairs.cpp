class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int>dp(n, 1000000);
        for(int i = 0; i < n; i++){
            dp[i] = cost[i];
            if(i > 1){
                dp[i] += min(dp[i - 1], dp[i - 2]);
            }
        }
        return min(dp[n - 1], dp[n - 2]);
    }
};