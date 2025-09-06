class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        subs = [s[i:i + 2] for i in range(len(s) - 1)]

        for sub in subs:
            if sub in s[::-1]:
                return True

        return False
