class Solution:
    def minOperations(self, s: str) -> int:
        pattern = '01' * len(s)

        start_zero = 0
        start_one = 0

        for i, j in zip(s, pattern):
            if i != j:
                start_zero += 1
            else:
                start_one += 1

        return min(start_zero, start_one)