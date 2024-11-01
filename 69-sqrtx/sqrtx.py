class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l,r  = 1, x // 2

        while l <= r:
            mid = l + (r-l) // 2 # this avoids int overflow in other languages
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid -1
            else:
                l = mid + 1

        return round(r)