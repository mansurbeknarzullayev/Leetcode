class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int ans = 0;
        int n = mat.size();
        int m = mat[0].size();
        vector<int>rc(n, 0), cc(m, 0);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                rc[i] += mat[i][j];
                cc[j] += mat[i][j];
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(rc[i] == 1 and cc[j] == 1 and mat[i][j] == 1){
                    ans ++;
                }
            }
        }
        return ans;
    }
};