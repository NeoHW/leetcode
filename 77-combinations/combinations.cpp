class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        // backtracking problem
        vector<vector<int>> ans;
        vector<int> currCombi;
        backtrack(ans,currCombi, n, k, 1);
        return ans;
    }

private:
    void backtrack(vector<vector<int>>& ans, vector<int>& currCombi, int n, int k, int start) {
        if (currCombi.size() == k) {
            ans.push_back(currCombi);
            return;
        }

        for (int i = start; i <= n; i++) {
            currCombi.push_back(i);
            backtrack(ans, currCombi, n, k, i+1);
            currCombi.pop_back();
        }
    }
};