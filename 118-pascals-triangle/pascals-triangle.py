class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue
            
            prev = res[-1]

            # first 1
            curr = [1]
            
            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j+1])

            # last 1
            curr.append(1)

            res.append(curr)
        
        return res
        