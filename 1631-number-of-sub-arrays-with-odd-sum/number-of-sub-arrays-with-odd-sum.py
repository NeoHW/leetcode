class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # even + even = even
        # odd + odd = even
        # odd + even = odd

        MOD = 1e9 + 7
        n = len(arr)
        dp_odd = n * [0]
        dp_even = n * [0]

        # convert arr to odd or even
        for i in range(n):
            arr[i] %= 2
        
        # initialise last element
        if arr[n-1] == 0:
            dp_even[n-1] = 1
        else:
            dp_odd[n-1] = 1

        # loop from back to front
        for i in range(n-2, -1, -1):
            if arr[i] == 1:
                # if curr element is odd, it flips parity of next one
                dp_odd[i] = (1 + dp_even[i+1]) % MOD
                dp_even[i] = dp_odd[i+1]
            else:
                # if curr element is even, if preserves parity 
                dp_even[i] = (1 + dp_even[i+1]) % MOD
                dp_odd[i] = dp_odd[i+1]
        
        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD
        
        return int(count)

