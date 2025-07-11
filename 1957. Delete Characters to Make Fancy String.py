class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = list(s[:2])

        for ch in s[2:]:
            if ch == ans[-1] and ch == ans[-2]:
                continue
            else:
                ans.append(ch)

        return ''.join(ans)
