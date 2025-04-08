class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Key idea: The repeated element must be removed, and to do that,
        we may need to remove everything before its first appearance.
        So, we go through the array from the end (right to left), keeping track of seen elements.
        As soon as we find a duplicate (an element we've already seen),
        we know we have to remove everything before this point.
        """

        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return (i // 3) + 1 # since each time we must remove 3 elements from front
            seen.add(nums[i])
        
        return 0