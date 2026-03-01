class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        ones = t.count('1')
        zeros = len(s) - ones
        ans = ''

        for ch in s:
            if ch == '0':
                if ones > 0:
                    ans += '1'
                    ones -= 1
                else:
                    ans += '0'
                    zeros -= 1
            else:
                if zeros > 0:
                    ans += '1'
                    zeros -= 1
                else:
                    ans += '0'
                    ones -= 1

        return ans
