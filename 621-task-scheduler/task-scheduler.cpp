class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // pq with cycle
        unordered_map<char, int> hm;
        for (char task : tasks) {
            hm[task]++;
        }

        priority_queue<int> pq;
        for (auto& [task, count] : hm) {
            pq.push(count);
        }
        
        int ans = 0;

        while (!pq.empty()) {
            vector<int> toAdd;
            int cycleLength = n + 1;

            for (int i = 0; i < cycleLength; i++) {
                if (!pq.empty()) {
                    toAdd.push_back(pq.top());
                    pq.pop();
                }
            }

            for (int count : toAdd) {
                if (--count > 0) {
                    pq.push(count);
                }
            }

            if (pq.empty()) {
                ans += toAdd.size();
            } else {
                ans += cycleLength;
            }
        }

        return ans;
    }
};