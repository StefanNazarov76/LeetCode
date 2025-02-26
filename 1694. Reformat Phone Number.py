class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        ans = []

        for i in range(0, len(number), 3):
            ans.append(number[i:i + 3])

        if len(ans[-1]) == 1:
            block = ans[-2] + ans[-1]

            ans.pop()
            ans.pop()

            ans.append(block[:2])
            ans.append(block[2:])

        return '-'.join(ans)
