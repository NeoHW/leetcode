class Solution {
public:
    int minLength(string sentence) {
        // use a stack , similar to matching paranthesis
        std::stack<char> s;

        for (char c : sentence) {
            if (s.empty()) {
                s.push(c);
                continue;
            }

            if ((c == 'B' && s.top() == 'A') || (c == 'D' && s.top() == 'C')) {
                s.pop();
            } else {
                s.push(c);
            }
        }

        return s.size();
    }
};