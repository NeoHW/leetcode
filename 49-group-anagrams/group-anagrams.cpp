class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, vector<string>> hm;
        vector<vector<string>> res;

        for (const auto& str : strs) {
            string temp = str;
            sort(temp.begin(), temp.end());
            hm[temp].push_back(str);
        }

        for (auto& pair : hm) {
            res.emplace_back(std::move(pair.second));
        }
        
        return res;
    }
};