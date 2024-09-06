class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            hm[sorted_s].append(s)
        
        
        return list(hm.values())
        # ans = []
        # for v in hm.values():
        #     ans.append(v)
        # return ans