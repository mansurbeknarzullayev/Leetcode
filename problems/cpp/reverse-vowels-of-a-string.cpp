class Solution {
public:
    bool isVowel(char c){
        c = tolower(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    string reverseVowels(string s) {
        vector<int>pos;
        for(int i = 0; i < s.length(); i++){
            if(isVowel(s[i])){
                pos.push_back(i);
            }
        }
        for(int i = 0; i < pos.size() / 2; i++){
            swap(s[pos[i]], s[pos[pos.size() - i - 1]]);
        }
        return s;
    }
};