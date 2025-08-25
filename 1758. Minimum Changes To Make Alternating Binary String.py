class Solution:
    def minOperations(self, s: str) -> int:
        prev = s[0]
        count = 0

        for i in range(1, len(s)):
            if s[i] == prev:
                prev = '0' if s[i] == '1' else '1'
                count += 1
            else:
                prev = s[i]

        return min(count, len(s) - count)
