class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            max_freq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])

                non_zero = [f for f in freq if f > 0]
                min_freq = min(non_zero)

                if max_freq == min_freq:
                    ans = max(ans, j - i + 1)

        return ans
