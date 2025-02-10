class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' in s:
            i = s.index('b')
        else:
            i = len(s)

        return s.count('a') <= i
