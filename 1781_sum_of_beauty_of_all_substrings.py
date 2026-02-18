class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = Counter()

            for j in range(i, n):
                freq[s[j]] += 1

                values = freq.values()
                ans += max(values) - min(values)

        return ans
