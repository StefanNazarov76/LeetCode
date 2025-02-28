class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(0, len(s) - 1):
            substring = s[i] + s[i + 1]

            if substring[::-1] in s:
                return True

        return False
