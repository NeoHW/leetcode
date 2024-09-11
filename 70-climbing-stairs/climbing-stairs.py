class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev, curr = 1, 2
        for i in range(3, n+1):
            temp = curr + prev
            prev = curr
            curr = temp
        
        return curr