class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []

        cell1, cell2 = s.split(':')
        r1, c1 = cell1
        r2, c2 = cell2

        for i in range(ord(r1), ord(r2) + 1):
            for j in range(int(c1), int(c2) + 1):
                ans.append(chr(i) + str(j))

        return ans