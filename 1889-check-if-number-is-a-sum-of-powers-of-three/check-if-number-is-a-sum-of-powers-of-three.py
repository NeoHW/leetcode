class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # two possible states when reducing by 3
        # either it is divisible by 3 directly, or 
        # it must be a sum of powers of 3 , which includes 3^0 = 1
        # e.g. 12 = 3^2 + 3^1 = 3(3^1 + 3^0) = 3(3^1 + 1)

        while n > 1:
            if n % 3 == 0 or (n-1) % 3 == 0:
                n //= 3
            else:
                return False
        
        return True