class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        n = len(words)
        ans = n

        for i, w in enumerate(words):
            if w == target:
                dist = min(abs(i - startIndex), n - abs(i - startIndex))
                ans = min(ans, dist)

        return ans
