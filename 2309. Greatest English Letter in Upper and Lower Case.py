class Solution:
    def greatestLetter(self, s: str) -> str:
        d = {}

        for i in set(s):
            if i.isupper() and i.lower() in s:
                d[i] = ord(i)

        if d:
            return max(d, key=d.get)
        else:
            return ''