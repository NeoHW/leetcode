class NumberContainers:

    def __init__(self):
        self.indexes = {} # maps index to their numbers
        self.map_to_pq = defaultdict(list) # maps each number to a PQ of indexes

    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        heapq.heappush(self.map_to_pq[number], index)

    def find(self, number: int) -> int:
        pq = self.map_to_pq[number]
        while (pq and self.indexes[pq[0]] != number):
            heapq.heappop(pq)
        
        return pq[0] if pq else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)