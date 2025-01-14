class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        res = 0

        for ch in s:
            if ch == '(':
                counter += 1
            elif ch == ')':
                counter -= 1

            res = max(res, counter)

        return res
