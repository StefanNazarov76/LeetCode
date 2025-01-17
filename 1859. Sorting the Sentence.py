class Solution:
    def sortSentence(self, s: str) -> str:
        res = [w for w in s.split()]

        for w in res.copy():
            res[int(w[-1]) - 1] = w[:-1]

        return ' '.join(res)
