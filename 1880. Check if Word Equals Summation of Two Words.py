class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_num = ''
        second_num = ''
        target_num = ''

        for i in firstWord:
            first_num += str(ord(i) - ord('a'))

        for i in secondWord:
            second_num += str(ord(i) - ord('a'))

        for i in targetWord:
            target_num += str(ord(i) - ord('a'))

        return int(first_num) + int(second_num) == int(target_num)
