class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0

        for ch in set(word):
            if ch.islower() and ch.upper() in word:
                ans += 1

        return ans
