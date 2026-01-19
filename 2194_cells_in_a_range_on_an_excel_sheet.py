class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(':')
        r1, c1 = s[0]
        r2, c2 = s[1]

        ans = []

        for r in range(ord(r1), ord(r2) + 1):
            for c in range(int(c1), int(c2) + 1):
                ans.append(chr(r) + str(c))

        return ans
