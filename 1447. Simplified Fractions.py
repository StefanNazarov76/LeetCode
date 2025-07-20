class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        for d in range(2, n + 1):
            for u in range(1, d):
                if gcd(u, d) == 1:
                    ans.append(f'{u}/{d}')
        return ans
