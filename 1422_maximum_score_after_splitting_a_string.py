class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0

        for i in range(len(s) - 1):
            left = s[0:i + 1]
            right = s[i + 1:]

            score = left.count('0') + right.count('1')

            ans = max(score, ans)

        return ans
