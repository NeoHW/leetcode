class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # every unique number = new colour

        hm = defaultdict(int)
        res = 0

        for num in answers:
            hm[num] += 1

        for k,v in hm.items():
            group_size = k+1 # as the rabbit does not include himself in the count
            
            # If more rabbits gave the same answer than the group can hold, we need multiple groups
            # So we divide v by group_size to find how many such full (or partially full) groups we need
            num_groups = ceil(v / group_size)
            res += num_groups * group_size
        
        return res