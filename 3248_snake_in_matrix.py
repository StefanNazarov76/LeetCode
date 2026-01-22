class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0

        for command in commands:
            if command == 'LEFT':
                pos -= 1
            elif command == 'RIGHT':
                pos += 1
            elif command == 'UP':
                pos -= n
            elif command == 'DOWN':
                pos += n

        return pos
