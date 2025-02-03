class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}

        for w in s1.split():
            if w not in d:
                d[w] = 0
            d[w] += 1

        for w in s2.split():
            if w not in d:
                d[w] = 0
            d[w] += 1

        return [k for k, v in d.items() if v == 1]
