class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = [i for i, ch in enumerate(s) if ch == c]
        ans = []
        pos_idx = 0

        for i in range(len(s)):
            dist = abs(i - positions[pos_idx])

            if pos_idx < len(positions) - 1 and dist > abs(i - positions[pos_idx + 1]):
                pos_idx += 1
                dist = abs(i - positions[pos_idx])

            ans.append(dist)

        return ans
