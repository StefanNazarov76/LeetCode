class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L_count = 0
        R_count = 0
        _count = 0

        for move in moves:
            if move == 'L':
                L_count += 1
            elif move == 'R':
                R_count += 1
            else:
                _count += 1

        return abs(L_count - R_count) + _count
