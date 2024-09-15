class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time_taken [1,1,12,8,3]
        # sort based on start positions : [10,8,5,3,0]
        # Time taken after being sorted based on start position: [1,1,8,3,12]
        # groups (1,8,12) -> total 3 groups

        time_taken = []
        for i in range(len(position)):
            time_to_reach_dst = (target - position[i]) / speed[i]
            time_taken.append((position[i], time_to_reach_dst))
        
        # sort by furthest first
        time_taken.sort(reverse=True)

        stack = []
        # create monotonic increasing stack
        for _, time in time_taken:
            if not stack or stack[-1] < time:
                stack.append(time)
        
        # return number of groups
        return len(stack)