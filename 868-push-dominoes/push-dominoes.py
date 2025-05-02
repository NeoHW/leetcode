class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # first pass, left to right to calculate right force
        force = 0
        for i,c in enumerate(dominoes):
            if c == 'R':
                force = n
            elif c == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
    
        # second pass, right to left to calculate left force
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L' for f in forces)