class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<int> dp(amount+1, amount+1); // initialise with amount+1 for easier use with min() later on
        dp[0] = 0; // no need coins to make amount 0

        for (int i = 1 ; i < amount+1; i++) {
            for (int coin : coins) {
                if (i - coin < 0) {
                    continue;
                }

                dp[i] = min(dp[i], dp[i-coin] + 1);
            }
        }

        return dp.back() != amount+1 ? dp.back() : -1;
    }
};