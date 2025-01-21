class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        stars = 0

        for i in range(0, len(s), 2):
            stars += s[i].count('*')

        return stars
