class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [''] * 10

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])

            rods[rod] += color

        ans = 0
        for i in rods:
            if 'R' in i and 'G' in i and 'B' in i:
                ans += 1

        return ans