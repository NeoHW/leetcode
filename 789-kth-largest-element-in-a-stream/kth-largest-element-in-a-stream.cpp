class KthLargest {
// we just need the top k elements in our PQ, and min heap it to get in O(1)

private:
    // std::greater<int> makes the max priority queue act as a min priority queue.
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;        

        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        if (pq.size() < k || pq.top() < val) {
            pq.push(val);
            // pop the smallest element out if size > k
            if (pq.size() > k) {
                pq.pop();
            }
        }
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */