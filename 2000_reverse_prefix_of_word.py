class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0

        if ch in word:
            i = word.index(ch)

        return word[:i + 1][::-1] + word[i + 1:]
