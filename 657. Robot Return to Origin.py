class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y += 1
            elif m == 'D':
                y -= 1

        return x == 0 and y == 0
