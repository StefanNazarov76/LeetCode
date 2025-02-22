class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        if k > len(s):
            k = k % len(s)

        left = s[k:]
        right = s[:k]

        return left + right