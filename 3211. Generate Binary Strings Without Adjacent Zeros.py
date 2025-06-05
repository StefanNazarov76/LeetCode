class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def r(s, rem):
            if rem == 0:
                ans.append(s)
                return

            if s[-1] != '0':
                r(s + '0', rem - 1)
            r(s + '1', rem - 1)

        r('0', n - 1)
        r('1', n - 1)

        return ans
