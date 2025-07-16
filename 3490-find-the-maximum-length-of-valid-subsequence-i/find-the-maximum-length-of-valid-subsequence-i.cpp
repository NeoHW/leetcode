class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int odd_count = 0;
        int even_count = 0;
        int alt_count = 0;
        int parity = -1;

        for (const auto& num: nums) {
            if (num % 2 == 0) {
                ++even_count;
                if (parity == 1 || parity == -1) {
                    ++alt_count;
                }
            } else {
                ++odd_count;
                if (parity == 0 || parity == -1) {
                    ++alt_count;
                }
            }

            parity = num % 2;
        }

        return std::max(std::max(even_count, odd_count), alt_count);
    }
};