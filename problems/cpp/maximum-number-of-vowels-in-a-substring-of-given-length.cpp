class Solution {
public:
    bool isVowel(char c){
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u';
    }
    int maxVowels(string s, int k) {
        int n = s.length();
        int ans = 0, cnt = 0;
        for(int i = 0; i < n; i++){
            if(isVowel(s[i])){
                cnt ++;
            }
            if(i >= k && isVowel(s[i - k])){
                cnt --;
            }
            ans = max(ans, cnt);
        }
        return ans;
    }
};