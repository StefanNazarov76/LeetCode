class Solution:
    def minOperations(self, s: str) -> int:
        start_zero = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    start_zero += 1
            else:
                if s[i] == '0':
                    start_zero += 1

        return min(start_zero, len(s) - start_zero)
