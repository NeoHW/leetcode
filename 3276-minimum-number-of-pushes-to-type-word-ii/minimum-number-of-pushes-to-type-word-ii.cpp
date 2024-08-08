class Solution {
public:
    int minimumPushes(string word) {
        unordered_map<char, int> frequency;
        // Count the frequency of each character
        for (char c : word) {
            frequency[c]++;
        }

        priority_queue<int> pq;
        for (const auto& entry : frequency) {
            pq.push(entry.second);
        }

        int totalPresses = 0;
        int keyIndex = 0; // 8,8,8,2

        while (!pq.empty()) {
            int freq = pq.top();
            pq.pop();

            // Determine the number of presses needed for the current key
            int pressesPerChar = (keyIndex / 8) + 1;
            totalPresses += freq * pressesPerChar;
            keyIndex++;
        }

        return totalPresses;
    }
};