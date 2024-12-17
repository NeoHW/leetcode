class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hm = Counter(s)
        pq = []
        res = []

        for char, count in hm.items():
            heapq.heappush(pq, (-ord(char), count)) # max heap of char

        while pq:
            c_ascii, count = heapq.heappop(pq)
            char = chr(-c_ascii)

            # add to res
            repeat = min(count, repeatLimit)
            res.append(char * repeat)
            count -= repeat

            if count > 0:
                if not pq: # no other characters available
                    break

                next_c_ascii, next_count = heapq.heappop(pq)
                next_char = chr(-next_c_ascii)
                res.append(next_char)
                next_count -= 1

                if next_count > 0:
                    heapq.heappush(pq, (next_c_ascii, next_count))
            
                heapq.heappush(pq, (c_ascii, count))

        return ''.join(res)
