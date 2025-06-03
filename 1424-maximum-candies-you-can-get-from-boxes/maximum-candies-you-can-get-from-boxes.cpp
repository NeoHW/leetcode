class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = status.size();
        vector<bool> has_box(n), has_key(n), opened(n);
        int res = 0;

        queue<int> q;
        for (int b : initialBoxes) {
            if (!has_box[b]) {
                has_box[b] = true;
                q.push(b);
            }
        }

        while (!q.empty()) {
            int b = q.front();
            q.pop();
            
            if (opened[b]) continue;

            if (status[b] == 1 || has_key[b]) {
                res += candies[b];
                opened[b] = true;

                // for every key inside box b
                for (int k : keys[b]) {
                    has_key[k] = true;
                    if (has_box[k] && !opened[k]) {
                        q.push(k);
                    }
                }

                // for every contained box inside box b
                for (int cb : containedBoxes[b]) {
                    if (!has_box[cb]) {
                        has_box[cb] = true;
                        q.push(cb);
                    }
                }
            }
        }

        return res;
        
    }
};