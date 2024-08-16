class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // maintain minHeap of k largest elements
        priority_queue<int, vector<int>, greater<int>> pq;

        for (int num : nums) {
            if (pq.size() < k) {
                pq.push(num);
            } else if (num > pq.top()) {
                pq.pop();
                pq.push(num);
            }
        }
        return pq.top();
    }
};