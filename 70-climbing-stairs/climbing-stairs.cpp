class Solution {
public:
    int climbStairs(int n) {
        // recursive relation: dp[n] = dp[n-1] + dp[n-2]
        if (n == 1) return 1;
        if (n == 2) return 2;

        // 1, 2, 3, 5, 8, 11
        int first = 1, second = 2;
        for (int i = 3; i <= n; i++) {
            int temp = first + second;
            first = second;
            second = temp;
        }

        return second;
    }
};