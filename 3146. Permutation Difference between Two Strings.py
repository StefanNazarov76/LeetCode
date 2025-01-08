class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0

        for s_index, ch in enumerate(s):
            t_index = t.index(ch)
            res += abs(s_index - t_index)

        return res
