class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow_freq = 0
        cons_freq = 0

        for i in set(s):
            count = s.count(i)

            if i in 'aeiou':
                vow_freq = max(vow_freq, count)
            else:
                cons_freq = max(cons_freq, count)

        return vow_freq + cons_freq