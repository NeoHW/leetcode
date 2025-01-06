class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        balls_to_left = 0
        shifts_from_left_needed = 0
        balls_to_right = 0
        shifts_from_right_needed = 0

        for i in range(n):
            # left pass
            res[i] += shifts_from_left_needed
            balls_to_left += int(boxes[i])
            shifts_from_left_needed += balls_to_left

            # right pass
            j = n - 1 - i
            res[j] += shifts_from_right_needed
            balls_to_right += int(boxes[j])
            shifts_from_right_needed += balls_to_right

        return res
