class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            if i > 9:
                k = str(i) + '#'
            else:
                k = str(i)

            if k in s:
                s = s.replace(k, chr(96 + i))

        return s
