class Solution:
    def candy(self, ratings: List[int]) -> int:
        # loop 3 times

        n = len(ratings)
        candies = [1] * n # start each child with 1 candy
        
        # first loop compare with LH neighbour (1 -> n-1) 
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # 2nd loop compare with RH neighbour (n-2 -> 0)
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        # last time to calculate number of candies
        return sum(candies)
