class Solution:
    def finalString(self, s: str) -> str:
        if 'i' not in s:
            return s

        ans = ''

        for ch in s:
            if ch == 'i':
                ans = ans[::-1]
            else:
                ans += ch

        return ans
