class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = ''

        for i, j in zip(s, s[::-1]):
            if i != j:
                res += chr(min(ord(i), ord(j)))
                continue

            res += i

        return res
