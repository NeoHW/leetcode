class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) < len(s):
            return False

        # append string to itself so that we can check circular property
        s = s + s

        substring = s[:len(goal)]

        for r in range(len(goal), len(s)):
            if substring == goal:
                return True
            substring = substring[1:] + s[r]
        
        return False