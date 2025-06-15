class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ''.join([w[0] for w in words])

        return ans == s