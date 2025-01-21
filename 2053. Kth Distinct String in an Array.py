class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        l = []

        for w in arr:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        for i, j in d.items():
            if j == 1:
                l.append(i)

        if len(l) >= k:
            return l[k - 1]
        else:
            return ''
