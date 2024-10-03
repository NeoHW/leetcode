class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        map<int, vector<int>> numToIndices; // store rank of each number in arr

        for (int i = 0; i < n; i++) {
            numToIndices[arr[i]].push_back(i);
        }
        
        int rank = 1;
        
        for (auto& pair : numToIndices) {
            for (int index : pair.second) {
                arr[index] = rank;
            }
            rank++;
        }

        return arr;
    }
};