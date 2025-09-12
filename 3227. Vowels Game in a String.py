class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(ch for ch in s if ch in 'aeiou')
