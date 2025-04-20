class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # every unique number = new colour

        hm = defaultdict(int)
        res = 0

        for num in answers:
            hm[num] += 1

        # if 3 rabbits say there are 1 other rabbits with the same colour, means there must be >1 colour, as max can be 2 per colour.
        for k,v in hm.items():
            # find total possible rabbits for that key - number of rabbits which answered (which is value)
            group_size = k+1
            num_groups = ceil(v / group_size)
            res += num_groups * group_size
        
        return res