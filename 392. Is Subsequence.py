class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for ch in s:
            for j in range(i, len(t)):
                if t[j] == ch:
                    i = j + 1
                    break
            else:
                return False

        return True
