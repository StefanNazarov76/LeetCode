class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0

        for index, letter in enumerate(s):
            ans += abs(index - t.index(letter))

        return ans
