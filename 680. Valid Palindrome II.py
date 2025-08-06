class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(x):
            return x == x[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pal(s[left + 1:right + 1]) or is_pal(s[left:right])

            left += 1
            right -= 1

        return True
