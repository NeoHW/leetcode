class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        stringstream ss1(sentence1), ss2(sentence2);
        string word;
        vector<string> s1Words, s2Words;
        while (ss1 >> word) s1Words.push_back(word);
        while (ss2 >> word) s2Words.push_back(word);

        if (s1Words.size() >= s2Words.size()) {
            swap(s1Words, s2Words);
        }

        int start = 0;
        int s1end = s1Words.size() - 1;
        int s2end = s2Words.size() - 1;

        // finding max number of words matching from start
        while (start < s1Words.size() && s1Words[start] == s2Words[start]) {
            ++start;
        }

        // finding max number of words matching in end
        while (s1end >= 0 && s1Words[s1end] == s2Words[s2end]) {
            --s1end;
            --s2end;
        }

        return s1end < start;
    }
};