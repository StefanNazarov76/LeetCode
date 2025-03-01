class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0

        for i in set(word.lower()):
            if i.upper() in word and i.lower() in word:
                ans += 1

        return ans