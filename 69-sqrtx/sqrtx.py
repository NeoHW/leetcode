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

        # when loop ends, l moved just past the possible values of the square root, meaning sqrt is somewhere below l
        # since r was last set to a value that was <= sqrt(x), we return r to get the cloest int approximation of sqrt(x) rounded down
        return round(r)