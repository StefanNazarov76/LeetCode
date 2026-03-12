class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        last = None

        for w, g in zip(words, groups):
            if g != last:
                ans.append(w)
                last = g

        return ans
