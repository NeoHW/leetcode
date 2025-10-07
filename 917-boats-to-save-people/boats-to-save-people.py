class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        l, r = 0, len(people) - 1

        # greedily pair largest and smallest, because if largest cannot pair with smallest, he cannot pair with anyone else
        while l <= r:
            if people[l] + people[r] > limit:
                l += 1
            else:
                l += 1
                r -= 1

            boats += 1
        
        return boats
