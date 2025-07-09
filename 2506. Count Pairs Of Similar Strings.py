class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = 0

        for i in range(len(words)):
            s = set(words[i])

            for j in range(i + 1, len(words)):
                if s == set(words[j]):
                    counter += 1

        return counter
