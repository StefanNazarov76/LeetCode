class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0

        for c in commands:
            if c == 'RIGHT':
                pos += 1
            elif c == 'LEFT':
                pos -= 1
            elif c == 'DOWN':
                pos += n
            else:
                pos -= n

        return pos
