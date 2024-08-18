class Solution {
public:
    int nthUglyNumber(int n) {
        // An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
        unordered_set<long long> hs;
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        vector<int> factors{2, 3, 5};
        
        // base case: 1 is the first ugly number
        pq.push(1);
        hs.insert(1);
        long long ans = 0;

        for (int count = 0; count < n; count++) {
            ans = pq.top();
            pq.pop();

            for (int factor : factors) {
                long long newUgly = ans * factor;
                if (!hs.contains(newUgly)) {
                    pq.push(newUgly);
                    hs.insert(newUgly);
                }
            }
        }

        return ans;
    }
};