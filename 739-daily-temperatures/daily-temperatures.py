class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # montonic decreasing stack
        n = len(temperatures)
        stack = []
        res = [0] * n

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, index))
                continue
            
            # pop out those in stack which are lower temp then curr: means found a warmer temp
            while stack and stack[-1][0] < temp:
                _, prevIndex = stack.pop()
                res[prevIndex] = index - prevIndex
            
            stack.append((temp,index))
        
        return res