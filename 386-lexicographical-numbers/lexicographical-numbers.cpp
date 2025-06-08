class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res;
        int curr = 1;

        for (int i = 0; i < n; ++i) {
            res.push_back(curr);

            // open subfolder (can we add 0 to our curr num, 1 -> 10 -> 100)
            if (curr * 10 <= n) {
                curr *= 10;
            } else {
                // go back up, removing last digit
                while (curr % 10 == 9 || curr >= n) {
                    curr /= 10;
                }
                ++curr; // 10 -> 11
            }
        }

        return res;
    }
};