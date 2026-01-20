class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        ans = 0

        for word in text:
            for ch in brokenLetters:
                if ch in word:
                    break
            else:
                ans += 1

        return ans
