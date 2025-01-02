class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = []
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix_sum.append(count)
        
        ans = [0] * len(queries)
        for i in range(len(queries)):
            start_idx, end_idx = queries[i]
            ans[i] = prefix_sum[end_idx] - (0 if start_idx == 0 else prefix_sum[start_idx - 1])
        
        return ans