class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int res = 0;
        string high_pair = x > y ? "ab" : "ba";
        string low_pair = high_pair == "ab" ? "ba" : "ab";

        string pass_one = removeSubstring(s, high_pair);
        int removed_pairs_one = (s.length() - pass_one.length()) / 2;
        res += removed_pairs_one * max(x, y);

        string pass_two = removeSubstring(pass_one, low_pair);
        int removed_pairs_two = (pass_one.length() - pass_two.length()) / 2;
        res += removed_pairs_two * min(x, y);

        return res;
    }

private:
    string removeSubstring(const string& input, const string& targetPair) {
        stack<char> char_stack;

        for (char c: input) {
            if (c == targetPair[1] && !char_stack.empty() && char_stack.top() == targetPair[0]) {
                char_stack.pop();
            } else {
                char_stack.push(c);
            }
        }

        string remaining;
        while (!char_stack.empty()) {
            remaining += char_stack.top();
            char_stack.pop();
        }

        reverse(remaining.begin(), remaining.end());
        return remaining;
    }
};