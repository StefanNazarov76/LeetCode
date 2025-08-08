class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[i] == s[j]:
                j += 1

            if j - i > 2:
                ans.append([i, j - 1])

            i = j

        return ans
