class Solution {
public:
    int minLength(string sentence) {
        // two pointers method, O(1) space
        int writePtr = 0;

        for (int readPtr = 0; readPtr < sentence.size(); ++readPtr) {
            // replace curr writePtr char with readPtr char
            sentence[writePtr] = sentence[readPtr];

            // check writePtr-1 and readPtr for valid removal pattern
            if (writePtr > 0 && 
                (sentence[writePtr-1] == 'A' || sentence[writePtr-1] == 'C') &&
                sentence[writePtr] == sentence[writePtr-1] + 1) {
                    --writePtr;
                } else {
                    ++writePtr;
                }
        }
        
        return writePtr;
        
        
        /*  
        // use a stack , similar to matching parenthesis
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
        */
    }
};