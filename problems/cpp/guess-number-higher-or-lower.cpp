/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *                1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long long l = 1;
        long long r = n + 1LL;
        while(r - l > 1){
            long long m = (l + r) / 2;
            int res = guess(m);
            if(res == 0){
                return m;
            }
            else if(res == 1){
                l = m;
            }
            else{
                r = m;
            }
        }
        return l;
    }
};