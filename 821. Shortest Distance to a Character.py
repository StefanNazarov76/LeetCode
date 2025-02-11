class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        indexes = []
        ans = []

        for i in range(n):
            if s[i] == c:
                indexes.append(i)

        for i in range(n):
            dist = []

            for j in indexes:
                dist.append(abs(i - j))
            ans.append(min(dist))

        return ans
