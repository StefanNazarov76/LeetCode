class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for w in words:
            res.extend(w.split(separator))

        return [w for w in res if w]
