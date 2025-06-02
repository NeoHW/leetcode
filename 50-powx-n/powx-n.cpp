class Solution {
public:
    double myPow(double x, int n) {
        double res = 1.0;
        long long power = n;

        if (power < 0) {
            x = 1/x;
            power = -power;
        }

        while (power > 0) {
            if (power % 2 == 1) {
                // If power is odd:
                // x^n = x * x^(n-1)
                res *= x;
            }

            // In every step:
            // We square x => x = x^2
            // We halve the power => power = power / 2
            // So effectively, we're doing: x^n = (x^(n/2))^2
            x *= x;
            power /= 2;
        }

        return res;
    }
};