class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = moves.count('R')
        l = moves.count('L')

        return len(moves) - 2 * min(r, l)
