class Solution {
public:
    string removeStars(string s) {
        string ans = "";
        int n = s.length();
        for(int i = 0; i < n; i++){
            if(s[i] == '*'){
                if(ans != "")ans.erase(--ans.end());
            }
            else{
                ans += s[i];
            }
        }
        return ans;
    }
};