class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            c = s[right]

            if c in count:
                count[c] += 1
            else:
                count[c] = 1

            while count[c] > 2:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
