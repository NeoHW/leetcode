class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for i in range(len(timePoints)):
            parts = timePoints[i].split(":")
            h,m = int(parts[0]), int(parts[1])
            minutes.append(h*60+m)
        
        minutes.sort()

        ans = float("inf")

        for i in range(1, len(timePoints)):
           ans = min(ans, minutes[i] - minutes[i-1])

        # consider difference between first and last element
        return min(ans, 24 * 60 - (minutes[-1] - minutes[0])) 

