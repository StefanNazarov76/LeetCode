class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0

        for freq in Counter(s).values():
            if freq % 2 == 0:
                ans += 2
            else:
                ans += 1

        return ans
