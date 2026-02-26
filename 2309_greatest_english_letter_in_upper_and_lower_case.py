class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s.upper())
        ans = []

        for l in letters:
            if l in s and l.lower() in s:
                ans.append(l)

        if ans:
            return sorted(ans)[-1]
        else:
            return ''
