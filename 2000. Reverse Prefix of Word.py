class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch)

            left = word[:index + 1]
            right = word[index + 1:]

            return left[::-1] + right

        else:
            return word
