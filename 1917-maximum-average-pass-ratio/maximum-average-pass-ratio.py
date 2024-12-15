class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # max heap by *change* in class ratio
        num_classes = len(classes)
        heap = []
        
        # heap contains (ratio change, class)
        for p,t in classes:
            ratio_change = (p+1)/(t+1) - (p/t)
            heapq.heappush(heap, (-ratio_change, (p,t)))
        
        for _ in range(extraStudents):
            _, c = heapq.heappop(heap)
            p,t = c[0], c[1]
            p += 1
            t += 1
            ratio_change = (p+1)/(t+1) - (p/t)
            heapq.heappush(heap, (-ratio_change, (p,t)))

        total_pass_ratio = 0

        for _, c in heap:
            p,t = c[0], c[1]
            total_pass_ratio += (p/t)
        
        return total_pass_ratio / num_classes