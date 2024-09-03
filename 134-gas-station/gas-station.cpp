class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        // if we start at A and get stuck at B, we won't be able to get to B from any station betweeen A and B
        int totalGas = 0;
        int currentGas = 0;
        int startIndex = 0;

        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i] - cost[i];
            currentGas += gas[i] - cost[i];

            if (currentGas < 0) {
                startIndex = i + 1;
                currentGas = 0;
            }
        }

        return totalGas < 0 ? -1 : startIndex;
    }
};