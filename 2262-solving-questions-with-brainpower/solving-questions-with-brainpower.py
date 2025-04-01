class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # Extra space for handling boundary cases

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            skip = dp[i + 1]
            solve = points + (dp[i + brainpower + 1] if i + brainpower + 1 < n else 0) # +1 as valid questions is AFTER brainpower 
            dp[i] = max(skip, solve)
        
        return dp[0] 
