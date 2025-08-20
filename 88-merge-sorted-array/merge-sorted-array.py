class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # dont have to store values in any buffer if we go backwards
        curr = m+n-1
        nums1_ptr = m-1
        nums2_ptr = n-1

        while nums2_ptr >= 0:
            if nums1_ptr >= 0 and nums1[nums1_ptr] >= nums2[nums2_ptr]:
                nums1[curr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[curr] = nums2[nums2_ptr]
                nums2_ptr -= 1

            curr -= 1
