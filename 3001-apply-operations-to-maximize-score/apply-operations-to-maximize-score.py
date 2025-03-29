class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        primes_score = [0] * n

        # sieve of eratosthenes
        primes = self.sieve(max(nums))

        # calculate prime score for each number in nums
        for index, num in enumerate(nums):
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime != 0:
                    continue
            
                primes_score[index] += 1
                while num % prime == 0:
                    num //= prime
            
            # if num is still greater than 1, it is a prime number itself
            if num > 1:
                primes_score[index] += 1
        
        # calculate the number of subarrays each number is dominant in using monotonic decreasing stack
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        stack = deque() 

        for index in range(n):
            while (stack and primes_score[stack[-1]] < primes_score[index]):
                top_index = stack.pop()
                next_dominant[top_index] = index
            
            # if stack not empty, set previous dominant element for current index
            if stack:
                prev_dominant[index] = stack[-1]
            
            stack.append(index)
    
        # Calculate the number of subarrays in which each element is dominant
        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]

        # Sort elements in decreasing order based on their values
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1

        # process elements while there are operations left
        processing_index = 0
        while k > 0:
            index,num = sorted_array[processing_index]
            processing_index += 1

            operations = min(k, num_of_subarrays[index])

            # use fast exponentiation
            score = (score * self.power(num, operations)) % self.MOD

            k -= operations
        
        return score

    def sieve(self, limit:int) -> list[int]:
        is_prime = [True] * (limit+1)
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime
        primes = []

        for num in range(2, limit + 1):
            if is_prime[num]:
                primes.append(num)
                for multiple in range(num*num, limit + 1, num):
                    is_prime[multiple] = False

        return primes
    
    def power(self, base, exponent):
        res = 1

        # Calculate the exponentiation using binary exponentiation
        while exponent > 0:
            # If the exponent is odd, multiply the result by the base
            if exponent % 2:
                res = (res * base) % self.MOD

            # Square the base and halve the exponent
            base = (base * base) % self.MOD
            exponent //= 2

        return res