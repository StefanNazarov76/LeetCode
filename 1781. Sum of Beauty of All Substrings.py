class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                counter = Counter(s[i:j + 1])
                ans += max(counter.values()) - min(counter.values())

        return ans
