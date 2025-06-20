class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 9, -1):
            pattern = str(i) + '#'

            if pattern in s:
                s = s.replace(pattern, chr(i + 96))

        for i in range(1, 10):
            pattern = str(i)

            if pattern in s:
                s = s.replace(pattern, chr(i + 96))

        return s
