class Solution:
    def partitionString(self, s: str) -> int:
        substring = set()
        ans = 1

        for ch in s:
            if ch in substring:
                substring.clear()
                ans += 1

            substring.add(ch)

        return ans
