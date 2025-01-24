class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0

        for ch in set(s):
            s_count = s.count(ch)
            t_count = t.count(ch)

            if s_count > t_count:
                res += s_count - t_count

        return res
