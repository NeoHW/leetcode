class Solution {
public:
    int getLucky(string s, int k) {
        int sum = 0, sum1 = 0;

        // transform 1
        for (char c : s) {
            int number = c - 'a' + 1;
            sum += number / 10 + number % 10;
        }
        k--;

        while (k-- > 0 && sum > 9) {
            for(; sum; sum /= 10) {
                sum1 += sum % 10;
            }
            swap(sum, sum1); // now sum will have updated value, and sum1 = 0
        }
        return sum;
    }
};