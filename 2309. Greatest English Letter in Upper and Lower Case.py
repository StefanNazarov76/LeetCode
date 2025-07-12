class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)

        letters = [l.upper() for l in s if l.lower() in s and l.upper() in s]
        letters.sort()

        if letters:
            return letters[-1]
        else:
            return ''
