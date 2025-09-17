class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0

        for d in str(num):
            if num % int(d) == 0:
                ans += 1

        return ans
