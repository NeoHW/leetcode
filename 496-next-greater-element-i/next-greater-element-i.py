class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonically decreasing stack
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                curr = stack.pop()
                next_greater[curr] = num
            
            stack.append(num)
        
        # for all those remaining in stack
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]