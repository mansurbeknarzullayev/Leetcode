class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ret = "";
        int n = word1.length();
        int m = word2.length();
        for(int i = 0; i < max(n, m); i++){
            if(i < n)ret += word1[i];
            if(i < m)ret += word2[i];
        }
        return ret;
    }
};