class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []

        for l in set(words[0]):
            m = min(w.count(l) for w in words)

            if m == 0:
                continue
            else:
                for _ in range(m):
                    res.append(l)

        return res
