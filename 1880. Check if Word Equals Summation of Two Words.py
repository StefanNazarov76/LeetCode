class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = ''.join(str(ord(i) - 97) for i in firstWord)
        b = ''.join(str(ord(i) - 97) for i in secondWord)
        c = ''.join(str(ord(i) - 97) for i in targetWord)

        return int(a) + int(b) == int(c)