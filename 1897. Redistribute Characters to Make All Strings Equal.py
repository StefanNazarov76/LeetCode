class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = ''.join(words)

        for _, freq in Counter(s).items():
            if freq % len(words) != 0:
                return False

        return True
