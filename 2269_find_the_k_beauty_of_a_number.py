class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_as_str = str(num)
        ans = 0

        for i in range(len(num_as_str) - k + 1):
            sub = int(num_as_str[i:i + k])

            if sub != 0 and num % sub == 0:
                ans += 1

        return ans
