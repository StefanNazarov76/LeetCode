class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        hh, mm = time.split(':')

        if mm[1] == '?':
            ans *= 10

        if mm[0] == '?':
            ans *= 6

        if hh[0] == '?' and hh[1] == '?':
            ans *= 24
        elif hh[1] == '?':
            if hh[0] == '2':
                ans *= 4
            else:
                ans *= 10

        elif hh[0] == '?':
            if hh[1] >= '4':
                ans *= 2
            else:
                ans *= 3

        return ans
