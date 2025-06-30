class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()

        ans = []
        for word, times in Counter(words).items():
            if times == 1:
                ans.append(word)

        return ans
