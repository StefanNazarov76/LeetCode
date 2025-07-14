class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        n = len(spaces)
        j = 0

        for i in range(len(s)):
            if j < n and i == spaces[j]:
                ans += ' '
                ans += s[i]
                j += 1
            else:
                ans += s[i]

        return ans
