class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # use 2 pointers as arrays are already sorted

        len1, len2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0 
        res = []

        while idx1 < len1 and idx2 < len2:
            nums1_id, nums1_val = nums1[idx1]
            nums2_id, nums2_val = nums2[idx2]
            
            if nums1_id == nums2_id:
                res.append([nums1_id, nums1_val + nums2_val])
                idx1 += 1
                idx2 += 1
            elif nums1_id < nums2_id:
                res.append([nums1_id, nums1_val])
                idx1 += 1
            else:
                res.append([nums2_id, nums2_val])
                idx2 += 1
        
        # add remaining nums in either array
        for i in range(idx1, len1):
            res.append([nums1[i][0], nums1[i][1]])

        for i in range(idx2, len2):
            res.append([nums2[i][0], nums2[i][1]])
        
        return res