class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = set()
        number = ''

        for i in word:
            if i.isdigit():
                number += i
            elif number:
                ans.add(int(number))
                number = ''

        if number:
            ans.add(int(number))

        return len(ans)
