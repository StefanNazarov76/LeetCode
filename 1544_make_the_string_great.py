class Solution:
    def makeGood(self, s: str) -> str:
        ans = []

        for ch in s:
            if ans and ch.islower() and ans[-1] == ch.upper():
                ans.pop()
            elif ans and ch.isupper() and ans[-1] == ch.lower():
                ans.pop()
            else:
                ans.append(ch)

        return ''.join(ans)
