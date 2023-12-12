class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>>v = grid;
        vector<int>mc(n, 0), mr(n, 0);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                mc[j] = max(mc[j], grid[i][j]);
                mr[i] = max(mr[i], grid[i][j]);
            }
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                ans += min(mc[j], mr[i]) - grid[i][j];
            }
        }
        return ans;
    }
};