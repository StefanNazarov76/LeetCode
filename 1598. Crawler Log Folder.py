class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for i in logs:
            if i == '../':
                ans -= 1
                if ans < 0:
                    ans = 0
            elif i == './':
                continue
            else:
                ans += 1

        return ans
