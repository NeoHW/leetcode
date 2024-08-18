class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        vector<char> open {'(', '[', '{'};

        for (char c : s) {
            if (find(open.begin(), open.end(), c) != open.end()) {
                st.push(c);
            } else {
                if (st.empty() || 
                    (c == ')' && st.top() != '(') ||
                    (c == ']' && st.top() != '[') ||
                    (c == '}' && st.top() != '{')) {
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};