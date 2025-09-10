class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        sign = - 1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            last_digit = (x % 10)
            reverse = reverse * 10 + last_digit
            x = x // 10
        reverse *= sign

        if reverse < -2 ** 31 or reverse > 2 ** 31 - 1:
            return 0
        else:
            return reverse
