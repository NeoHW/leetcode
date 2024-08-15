class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> curr;
        
        dfs(candidates, target, curr, ans, 0, 0);
        return ans;
    }

private:
    void dfs(vector<int>& candidates, int target, vector<int>& curr, vector<vector<int>>& ans, int currSum, int index) {
        if (currSum == target) {
            ans.push_back(curr);
            return;
        }

        if (currSum > target || index >= candidates.size()) {
            return;
        }

        // include or dont include current
        curr.push_back(candidates[index]);
        dfs(candidates, target, curr, ans, currSum + candidates[index], index);
        curr.pop_back();
        dfs(candidates, target, curr, ans, currSum, index+1);
    }
};