class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''

        for i in s:
            number += str(ord(i) - 96)

        for i in range(k):
            temp = 0
            for j in number:
                temp += int(j)
            number = str(temp)

        return int(number)
