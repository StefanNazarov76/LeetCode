class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        a = []
        for b in words:
            for c in b.split(separator):
                if c:
                    a.append(c)
        return a
