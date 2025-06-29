class Solution:
    def sortString(self, s: str) -> str:
        ans = ''
        s = list(s)

        while s:
            unique_chars = list(set(s))
            for i in sorted(unique_chars):
                ans += i
                s.remove(i)

            unique_chars = list(set(s))
            for i in sorted(unique_chars, reverse=True):
                ans += i
                s.remove(i)

        return ans
