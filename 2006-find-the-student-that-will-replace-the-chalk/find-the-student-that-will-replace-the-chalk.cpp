class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long sum = 0;
        for (int c : chalk) {
            sum += c;
        }

        // so that we can one pass it
        k %= sum;

        for (int i = 0; i < chalk.size(); i++) {
            if (k < chalk[i]) {
                return i;
            }
            k -= chalk[i];
        }
        
        return chalk.size()-1;
    }
};