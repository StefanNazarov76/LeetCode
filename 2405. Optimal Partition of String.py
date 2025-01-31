class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        substring = ''

        for ch in s:
            if ch in substring:
                res += 1
                substring = ''

            substring += ch

        return res
