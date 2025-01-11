class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        counts = Counter(s)
        odd_count = 0
        for _,v in counts.items():
            if v % 2 != 0:
                odd_count += 1
        
        # If number of odd letters count is k, we must minimally make k palindromes
        # Therefore, if number of odd-freq chars >k, impossible to form k palindromes
        if odd_count > k:
            return False

        return True