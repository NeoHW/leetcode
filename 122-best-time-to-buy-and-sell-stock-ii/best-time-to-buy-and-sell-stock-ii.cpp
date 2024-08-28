class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // we buy on day i as long as next day (i+1) goes up
        // sell on day i when day i+1 decreases

        int maxProfit = 0;
        bool bought = false;
        int buyPrice;

        for (int i = 0; i < prices.size()-1; i++) {
            if (prices[i] < prices[i+1] && !bought) {
                buyPrice = prices[i];
                bought = true;
                continue;
            }

            if (prices[i] > prices[i+1] && bought) {
                maxProfit += prices[i] - buyPrice;
                bought = false;
                continue;
            }
        }

        // handle the case of last element
        if (bought) {
            maxProfit += prices.back() - buyPrice;
        }

        return maxProfit;

    }
};