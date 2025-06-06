class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0

        l_count = 0
        r_count = 0

        for i in s:
            if i == "L":
                l_count += 1
            else:
                r_count += 1

            if l_count == r_count:
                ans += 1

        return ans
