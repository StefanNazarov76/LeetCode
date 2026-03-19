class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        for freq in (counter1 - counter2).values():
            if freq > 3:
                return False

        for freq in (counter2 - counter1).values():
            if freq > 3:
                return False

        return True
