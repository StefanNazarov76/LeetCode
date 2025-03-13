class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)

        for w in words:
            p = tuple(ord(s) - ord(f) for f, s in pairwise(w))
            d[p].append(w)

        for k in d.values():
            if len(k) == 1:
                return k[0]