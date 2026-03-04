class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        seen = set()
        ans = []

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if j / i not in seen:
                    seen.add(j / i)
                    ans.append(f'{i}/{j}')

        return ans
