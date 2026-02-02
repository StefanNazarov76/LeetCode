class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        for i in range(len(words) - 1):
            prefix = words[i]

            for j in range(i + 1, len(words)):
                if words[j].startswith(prefix) and words[j].endswith(prefix):
                    ans += 1

        return ans
