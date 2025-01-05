class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_arr = [0] * n

        # Cumulative sums difference array that just stores how many more shifts should be applied to the current character instead of the previous one. Just need to record starting and ending point of shifts
        for start, end, direction in shifts:
            if direction == 1:
                diff_arr[start] += 1
                if end + 1 < n:
                    diff_arr[end + 1] -= 1
            else:
                diff_arr[start] -= 1
                if end + 1 < n:
                    diff_arr[end + 1] += 1
        
        res = []
        number_of_shifts = 0
        
        for i in range(n):
            number_of_shifts = (number_of_shifts + diff_arr[i]) % 26
            if number_of_shifts < 0:
                number_of_shifts += 26 # ensure non-negative shifts
            
            shifted_char = chr((ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a"))
            res.append(shifted_char)
        
        return "".join(res)