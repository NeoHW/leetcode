class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> curr;
        sort(candidates.begin(), candidates.end());

        backtrack(ans, curr, candidates, target, 0);
        return ans;
    }

private:
    void backtrack(vector<vector<int>>& ans, vector<int>& curr, vector<int>& candidates, int target, int index) {
        if (target == 0) {
            ans.push_back(curr);
            return;
        }

        // starts at current index to end as long as target >= candidates[i]
        for (int i = index; i < candidates.size() && target >= candidates[i]; i++) {
            // to avoid duplicates
            // either pick the first candidate or skips the current candidate if it’s same as previous one
            if (i == index || candidates[i] != candidates[i-1]) {
                curr.push_back(candidates[i]);
                backtrack(ans, curr, candidates, target - candidates[i], i + 1);
                curr.pop_back();
            }
        }
    }
};