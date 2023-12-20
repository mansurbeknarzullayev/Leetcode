class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        vector<int>vec;
        int n = prices.size();
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                vec.push_back(prices[i] + prices[j]);
            }
        }
        int left = 0;
        int ok = false;
        for(int i = 0; i < vec.size(); i++){
            if(money - vec[i] >= 0){
                left = max(left, money - vec[i]);
                ok = true;
            }
        }
        return ok ? left : money;
    }
};