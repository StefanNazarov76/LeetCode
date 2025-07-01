class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()

        ans = len(words)
        for w in words:
            for l in brokenLetters:
                if l in w:
                    ans -= 1
                    break

        return ans
