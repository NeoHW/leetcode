class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # montonic decreasing stack
        n = len(temperatures)
        stack = []
        res = [0] * n

        for index, currTemp in enumerate(temperatures):
            if not stack:
                stack.append(index)
                continue
            
            # pop out those in stack which are lower temp then curr: means found a warmer temp
            while stack and temperatures[stack[-1]] < currTemp:
                prevIndex = stack.pop()
                res[prevIndex] = index - prevIndex
            
            stack.append(index)
        
        return res