class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        counter = 0
        for w in counter1:
            if counter1[w] == 1 and counter2[w] == 1:
                counter += 1

        return counter