class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = list(s)

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    ans[right] = s[left]

                else:
                    ans[left] = s[right]

            left += 1
            right -= 1

        return ''.join(ans)
