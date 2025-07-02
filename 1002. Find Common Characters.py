class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []

        for c in set(words[0]):
            min_count = words[0].count(c)

            for w in words[1:]:
                min_count = min(min_count, w.count(c))

            ans.extend([c] * min_count)

        return ans
