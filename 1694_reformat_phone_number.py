class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n = len(number)
        ans = []
        i = 0

        if len(number) % 3 == 1:
            n = len(number) - 4
        elif len(number) % 3 == 2:
            n = len(number) - 2

        while i < len(number):
            if i < n:
                ans.append(number[i:i + 3])
                i += 3
            else:
                ans.append(number[i:i + 2])
                i += 2

        return '-'.join(ans)