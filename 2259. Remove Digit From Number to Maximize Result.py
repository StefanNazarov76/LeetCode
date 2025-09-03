class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0

        for i, n in enumerate(number):
            if n == digit:
                removed = int(number[:i] + number[i + 1:])
                res = max(res, removed)

        return str(res)
