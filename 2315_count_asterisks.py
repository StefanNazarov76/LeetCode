class Solution:
    def countAsterisks(self, s: str) -> int:
        s_without_pairs = ''
        bars = 0

        for ch in s:
            if ch == '|':
                bars += 1

            if bars % 2 == 0:
                s_without_pairs += ch

        return s_without_pairs.count('*')
