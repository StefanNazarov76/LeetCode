class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for i in logs:
            if i == './':
                continue
            elif i == '../':
                ans -= 1
            else:
                ans += 1

            if ans < 0:
                ans = 0

        return ans
