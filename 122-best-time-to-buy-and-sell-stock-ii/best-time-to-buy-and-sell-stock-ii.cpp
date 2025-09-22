class Solution {
public :
	long long maxProfit(vector<int>& prices) {
        long long ans = 0;
        for (int i = 1; i < prices.size(); ++i)
            if (prices[i] > prices[i-1]) {
                ans += (long long)prices[i] - prices[i-1];
            }
        return ans;
	}
};