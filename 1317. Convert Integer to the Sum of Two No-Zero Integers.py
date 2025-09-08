class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(num):
            while num:
                temp = num % 10
                if temp == 0:
                    return False
                num //= 10

            return True

        for b in range(1, n):
            a = n - b

            if check(a) and check(b):
                return [a, b]
