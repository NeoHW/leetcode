class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # merge interval type of qn
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            letter_index = ord(c) - ord("a")
            if first[letter_index] == -1:
                first[letter_index] = i
            last[letter_index] = i
        
        res = []
        partition_start, partition_end = 0,0

        for i,c in enumerate(s):
            letter_index = ord(c) - ord("a")
            partition_end = max(partition_end, last[letter_index])

            if i == partition_end: # found a partition
                res.append(partition_end - partition_start + 1)
                partition_start = i + 1
        
        return res