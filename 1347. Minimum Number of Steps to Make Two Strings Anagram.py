class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0

        for i in set(s):
            s_count = s.count(i)
            t_count = t.count(i)

            if s_count > t_count:
                ans += s_count - t_count

        return ans
