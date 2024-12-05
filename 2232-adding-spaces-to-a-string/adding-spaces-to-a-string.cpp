class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string ans = "";
        int spacesIndex = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (spacesIndex < spaces.size() && i == spaces[spacesIndex]) {
                ans += " ";
                ++spacesIndex;
            }
            ans += s[i];
        }
        return ans;
    }
};