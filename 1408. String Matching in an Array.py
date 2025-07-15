class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()

        for w in words:
            for s in words:
                if w != s and s in w:
                    ans.add(s)

        return list(ans)
