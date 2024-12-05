class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int lengthStr1 = str1.size(), lengthStr2 = str2.size();

        int ptr2 = 0;

        for (int ptr1 = 0; ptr1 < lengthStr1 && ptr2 < lengthStr2; ++ptr1) {
            if (str1[ptr1] == str2[ptr2] || str1[ptr1] + 1 == str2[ptr2] || str1[ptr1] - 25 == str2[ptr2]) {
                ++ptr2;
            }
        }

        return ptr2 == lengthStr2;
    }
};