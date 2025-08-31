class Solution:
    def concatHex36(self, n: int) -> str:
        n2 = n * n
        n3 = n * n * n

        ans1 = []
        ans2 = []

        while n2 > 0:
            remainder = n2 % 16
            n2 = int(n2 / 16)

            if remainder > 9:
                ans1.append(chr(55 + remainder))
            else:
                ans1.append(str(remainder))

        ans1.reverse()

        while n3 > 0:
            remainder = n3 % 36
            n3 = int(n3 / 36)

            if remainder > 9:
                ans2.append(chr(55 + remainder))
            else:
                ans2.append(str(remainder))

        ans2.reverse()

        return ''.join(ans1 + ans2)
