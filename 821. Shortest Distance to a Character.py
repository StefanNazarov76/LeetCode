class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = [i for i, char in enumerate(s) if char == c]

        ans = []
        for i in range(len(s)):
            distance = min(abs(i - j) for j in indexes)
            ans.append(distance)

        return ans
