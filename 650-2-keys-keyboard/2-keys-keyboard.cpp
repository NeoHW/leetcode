class Solution {
public:
    int minSteps(int n) {
        // prime factorisation of numbers
        // 24 = 2 * 2 * 2 * 3; ans: 2 + 2 + 2 + 3 = 9

        if (n == 1) return 0;

        int count = 0, factor = 2;

        while (n > 1) {
            while (n % factor == 0) {
                n /= factor;
                count += factor;
            }
            factor++;
        }

        return count;
    }
};