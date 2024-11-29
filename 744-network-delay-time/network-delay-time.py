class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # find the max in array of dijkstra
        INF = float("inf")

        AL = [[] for _ in range(n+1)]
        for source, target, time in times:
            AL[source].append([target, time])
        
        dist = [INF] * (n + 1)
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0,k))

        while pq:
            d,u = heapq.heappop(pq) # shortest unvisited u
            if d > dist[u]: # very important check
                continue
            for neighbour, time in AL[u]:
                if dist[u] + time >= dist[neighbour]: # dosen't improve timing
                    continue
                dist[neighbour] = dist[u] + time # relax operation
                heapq.heappush(pq, (dist[neighbour], neighbour))
        
        max_time = max(dist[1:])
        return -1 if max_time == INF else max_time