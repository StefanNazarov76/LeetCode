class Solution:
    def countPoints(self, rings: str) -> int:
        rods = ['', '', '', '', '', '', '', '', '', '']
        res = 0

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])

            rods[rod] += color

        for rod in rods:
            if 'R' in rod and 'G' in rod and 'B' in rod:
                res += 1

        return res
