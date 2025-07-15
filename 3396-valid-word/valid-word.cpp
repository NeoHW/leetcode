class Solution {
public:
    bool isValid(string word) {
        if (word.size() < 3) return false;

        bool has_vowel = false;
        bool has_const = false;

        for (auto c: word) {
            if (!std::isalnum(c)) return false;

            c = std::tolower(c);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                has_vowel = true;
            } else if (std::isalpha(c)) {
                has_const = true;
            }
        }

        return has_vowel && has_const;
    }
};