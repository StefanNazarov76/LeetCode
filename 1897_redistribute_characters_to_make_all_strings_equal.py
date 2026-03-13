class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        words = ''.join(words)

        for freq in Counter(words).values():
            if freq % n != 0:
                return False

        return True
