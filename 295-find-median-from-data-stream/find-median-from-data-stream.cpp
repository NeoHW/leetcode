class MedianFinder {
public:
    // keep 2 heaps , one min one max of equal sizes
    priority_queue<int> maxHeap;
    priority_queue <int, vector<int>, greater<int>> minHeap;

    MedianFinder() {
        
    }
    
    void addNum(int num) {
        maxHeap.push(num);
        
        // balance the heaps 
        minHeap.push(maxHeap.top());
        maxHeap.pop();

        // ensure maxHeap cah have 1 more element than minHeap
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.top();
        } else {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */