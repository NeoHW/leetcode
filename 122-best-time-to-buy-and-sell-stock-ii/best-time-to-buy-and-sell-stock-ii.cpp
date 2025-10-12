class Solution {
private:
    long long NEG_INF = -1e14;

public:
    long long maxProfit(vector<int>& prices) {
        long long cash = 0;
        long long hold = NEG_INF;

        for (int p : prices) {
            long long new_cash = std::max(cash, hold + p);
            long long new_hold = std::max(hold, cash - p);

            cash = new_cash;
            hold = new_hold;
        }
        return cash;
    }
};
