class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0

        for freq in Counter(s).values():
            if freq % 2 == 0:
                ans += freq
            elif ans % 2 == 0:
                ans += freq
            else:
                ans += freq - 1

        return ans
