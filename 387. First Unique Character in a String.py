class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1

        for k, v in d.items():
            if v == 1:
                return s.index(k)

        return -1