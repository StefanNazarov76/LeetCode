class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getValue(word):
            value = ''

            for ch in word:
                value += str(ord(ch) - 97)

            return int(value)

        return getValue(firstWord) + getValue(secondWord) == getValue(targetWord)
