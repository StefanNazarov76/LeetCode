class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        left_count = [0] * n
        seen_left = set()
        for i in range(n):
            seen_left.add(s[i])
            left_count[i] = len(seen_left)

        right_count = [0] * n
        seen_right = set()
        for i in range(n - 1, -1, -1):
            seen_right.add(s[i])
            right_count[i] = len(seen_right)

        counter = 0
        for i in range(n - 1):
            if left_count[i] == right_count[i + 1]:
                counter += 1

        return counter
