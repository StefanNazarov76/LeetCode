class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        l_count = 0
        r_count = 0

        for ch in s:
            if ch == 'L':
                l_count += 1
            else:
                r_count += 1

            if l_count == r_count:
                res += 1

        return res
