class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles) 
        hs = set()
        used = [False] * n

        self.dfs(tiles, "", hs, used)

        return len(hs) - 1
    
    def dfs(self, tiles: str, current: str, hs: set, used: list) -> None:
        hs.add(current)

        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self.dfs(tiles, current+char, hs, used)
                used[pos] = False