class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve_arr = self.sieve(right)
        primes = [num for num in range(left,right + 1) if sieve_arr[num]]

        closest_pair = (-1, -1)
        if len(primes) < 2:
            return closest_pair
        
        # find smallest difference between pairs
        min_diff = float("inf")

        for i in range(len(primes) - 1):
            diff = primes[i+1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = primes[i], primes[i+1]
        
        return closest_pair

    # use sieve of eratosthenes
    def sieve(self, limit:int):
        sieve = [True] * (limit+1)
        sieve[0] = sieve[1] = False # 0 and 1 are not prime

        for num in range(2, int(limit**0.5) + 1):
            if sieve[num]:
                for multiple in range(num*num, limit + 1, num):
                    sieve[multiple] = False
        return sieve