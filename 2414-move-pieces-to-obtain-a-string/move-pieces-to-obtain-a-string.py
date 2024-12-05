class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        s_index, t_index = 0, 0

        while s_index < n or t_index < n:
            while t_index < n and target[t_index] == '_':
                t_index += 1
            while s_index < n and start[s_index] == '_':
                s_index += 1

            if s_index >= n and t_index >= n:
                return True
            
            if (s_index >= n and t_index < n) or (t_index >= n and s_index < n):
                return False

            if start[s_index] != target[t_index]:
                return False
            
            letter = start[s_index]

            # L can only move left and not right
            if letter == 'L' and s_index < t_index:
                return False

            # R can only move right and not left
            if letter == 'R' and s_index > t_index:
                return False

            t_index += 1
            s_index += 1
        
        return True