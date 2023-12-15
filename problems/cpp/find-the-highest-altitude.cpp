class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0;
        int cur = 0;
        int n = gain.size();
        for(int i = 0; i < n; i++){
            cur += gain[i];
            ans = max(ans, cur);
        }
        return ans;
    }
};