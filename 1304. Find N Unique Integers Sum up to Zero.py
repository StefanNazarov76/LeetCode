class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        total = 0

        for i in range(1, n):
            ans.append(i)
            total += i

        ans.append(-total)
        return ans
