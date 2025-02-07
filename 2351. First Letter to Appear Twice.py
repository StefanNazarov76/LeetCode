class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            if s[:i].count(s[i]) == 1:
                return s[i]
