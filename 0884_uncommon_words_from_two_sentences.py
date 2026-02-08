class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        ans = []

        for w in s1:
            if w not in s2 and s1.count(w) == 1:
                ans.append(w)

        for w in s2:
            if w not in s1 and s2.count(w) == 1:
                ans.append(w)

        return ans
