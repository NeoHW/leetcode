class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int> hm;
        int res {-1};
        
        for (const int& num: arr) {
            hm[num]++;
        }

        for (auto &[key,value] : hm) {
            if (key == value) {
                res = max(res, key);
            }
        }

        return res;
    }
};