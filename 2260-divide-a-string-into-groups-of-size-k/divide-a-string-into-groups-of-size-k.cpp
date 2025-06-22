class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.size();
        vector<string> res;
        for (int i = 0; i < n; i += k) {
            string temp {};
            for (int j = 0; j < k; ++j) {
                if (i+j < n) {
                    temp += s[i+j];
                } else {
                    temp += fill;
                }
            }
            res.push_back(temp);
        }
        return res;
    }
};