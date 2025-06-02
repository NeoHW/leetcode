class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1); // each child start with 1

        // compare to left neighbour
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i-1]) {
                candies[i] = candies[i-1] + 1;
            }
        }

        // compare to right neighbour
        for (int i = n-2; i >= 0; --i) {
            if (ratings[i] > ratings[i+1]) {
                // if have a higher rating than their RH neighbour, they will get 1 more candy than RH neighbour unless they already have more candies than their RH
                candies[i] = max(candies[i], candies[i+1] + 1);
            }
        }

        int res = 0;
        for (int c : candies) {
            res += c;
        }

        return res;
    }
};