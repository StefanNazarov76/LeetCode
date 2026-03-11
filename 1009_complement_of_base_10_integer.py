class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        ans = ''

        for d in binary:
            if d == '1':
                ans += '0'
            else:
                ans += '1'

        return int(ans, 2)
