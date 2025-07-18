class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        unmatched_cnt = 0

        for i in s:
            if i == '(':
                open_cnt += 1
            else:
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    unmatched_cnt += 1

        return open_cnt + unmatched_cnt
