class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0

        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    counter += 1

        return counter
