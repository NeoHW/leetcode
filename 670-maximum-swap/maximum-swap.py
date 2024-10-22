class Solution:
    def maximumSwap(self, num: int) -> int:
        # find the largest maximum we can swap with
        numstr = list(str(num))
        n = len(numstr)

        maxRightIndex = [0] * n # store index of largest element (right-most) from i to end of string
        maxRightIndex[n-1] = n-1

        # populate maxRightIndex array from backwards
        for i in range(n-2, -1, -1):
            maxRightIndex[i] = i if numstr[i] > numstr[maxRightIndex[i+1]] else maxRightIndex[i+1]
        
        # forward pass to find swap
        for i in range(n):
            # we swap only if it is a bigger number
            if numstr[i] < numstr[maxRightIndex[i]]:
                numstr[i], numstr[maxRightIndex[i]] = numstr[maxRightIndex[i]] , numstr[i]
                return int("".join(numstr))
        
        return num



    # TRICKY TESTCASES:
    # 1993
    # 98368