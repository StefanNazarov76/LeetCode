class Solution:
    def modifyString(self, s: str) -> str:
        ans = []

        for i, ch in enumerate(s):
            if ch == '?':
                j = ord('a')
                while (ans and chr(j) == ans[-1]) or (i < len(s) - 1 and chr(j) == s[i+1]):
                    j += 1
                ans.append(chr(j))
            else:
                ans.append(ch)

        return ''.join(ans)
