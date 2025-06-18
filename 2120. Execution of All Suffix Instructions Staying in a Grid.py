class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []

        for i in range(len(s)):
            row, col = startPos
            counter = 0

            for j in s[i:]:
                if j == 'U':
                    row -= 1
                elif j == 'D':
                    row += 1
                elif j == 'R':
                    col += 1
                else:
                    col -= 1

                if row < 0 or row == n or col < 0 or col == n:
                    break
                counter += 1

            ans.append(counter)

        return ans
