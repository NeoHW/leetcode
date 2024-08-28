class Solution {
public:
    long long ans = 0;
    int s;
    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        vector<vector<int>> AL(roads.size() + 1);
        s = seats;

        for (vector<int> r : roads) {
            AL[r[0]].push_back(r[1]);
            AL[r[1]].push_back(r[0]);
        }

        dfs(0, 0, AL);
        return ans;
    }

    int dfs(int i, int prev, vector<vector<int>>& AL, int people = 1) {
        for (int neighbour : AL[i]) {
            if (neighbour == prev) continue;
            people += dfs(neighbour, i, AL);
        }
        if (i != 0) {
            ans += (people % s == 0 ? people/s : people/s +1);
        }
        return people;
    }
};