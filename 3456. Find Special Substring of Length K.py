class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        for i in range(n - k + 1):
            ch = s[i]

            if s[i:i + k] != ch * k:
                continue

            if i > 0 and s[i - 1] == ch:
                continue

            if i + k < n and s[i + k] == ch:
                continue

            return True

        return False
