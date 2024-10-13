class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        target_arrival_time = times[targetFriend][0]

        arrival_times = []
        avail_chairs = list(range(n))

        for i in range(n):
            arrival_time, leaving_time = times[i]
            heapq.heappush(arrival_times, (arrival_time, leaving_time, i)) # arrival time, leaving time and person index

        leaving_heap = []

        while arrival_times:
            current_time = arrival_times[0][0]

            # can have more than 1 leaving time
            while leaving_heap and leaving_heap[0][0] <= current_time:
                _, chair = heapq.heappop(leaving_heap)
                heapq.heappush(avail_chairs, chair)

            # unique arrival time
            if arrival_times and arrival_times[0][0] == current_time:
                arrival_time, leaving_time, person_index = heapq.heappop(arrival_times)
                chair = heapq.heappop(avail_chairs)
                
                if person_index == targetFriend:
                    return chair
                
                heapq.heappush(leaving_heap, (leaving_time, chair)) # leaving time and chair
        
        return -1