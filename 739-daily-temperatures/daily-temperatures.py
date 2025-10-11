class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use index in monotonically decreasing stack
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res