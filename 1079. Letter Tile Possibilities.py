class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()

        for i in range(1, len(tiles) + 1):
            for j in itertools.permutations(tiles, i):
                ans.add(j)

        return len(ans)