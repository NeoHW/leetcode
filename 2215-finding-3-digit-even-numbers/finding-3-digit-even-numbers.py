class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # check each even number from 100 - 999 to see if it can be created

        def canBeFormed(num: int) -> bool:
            count_arr = [0] * 10
            while num != 0:
                count_arr[num%10] += 1
                num //= 10
            
            for i,v in enumerate(count_arr):
                if hm[i] < v:
                    return False

            return True

        res = []
        hm = Counter(digits)

        for num in range(100, 1000, 2):
            if canBeFormed(num):
                res.append(num)
        
        return res
    
