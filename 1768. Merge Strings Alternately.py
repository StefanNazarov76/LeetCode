class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))

        ans = ''
        for i in range(n):
            if i >= len(word1):
                ans += word2[i:]
                break

            if i >= len(word2):
                ans += word1[i:]
                break

            ans += word1[i]
            ans += word2[i]

        return ans
