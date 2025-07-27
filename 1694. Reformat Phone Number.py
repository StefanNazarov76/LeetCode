class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')

        ans = []
        if len(number) % 3 == 0:
            for i in range(0, len(number), 3):
                ans.append(number[i:i + 3])

        elif len(number) % 3 == 1:
            for i in range(0, len(number) - 4, 3):
                ans.append(number[i:i + 3])

            ans.append(number[-4:-2])
            ans.append(number[-2:])

        else:
            for i in range(0, len(number) - 2, 3):
                ans.append(number[i:i + 3])

            ans.append(number[-2:])

        return '-'.join(ans)
