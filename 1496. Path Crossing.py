class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = [(0, 0)]

        for i in path:
            x, y = locations[-1]

            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1

            if (x, y) in locations:
                return True
            else:
                locations.append((x, y))

        return False
