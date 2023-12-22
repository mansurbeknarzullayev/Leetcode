class Solution {
public:
    int maxScore(string s) {
        int l = 0;
        int r = 0;
        int ans = 0;
        int n = s.length();
        for(int i = 0; i < n; i++){
            if(s[i] == '1'){
                r ++;
            }
        }
        for(int i = 0; i < n - 1; i++){
            if(s[i] == '0'){
                l ++;
            }
            else{
                r --;
            }
            ans = max(ans, l + r);
        }
        return ans;
    }
};