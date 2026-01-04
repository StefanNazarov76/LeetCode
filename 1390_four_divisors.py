class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            divisors = set()

            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                    if len(divisors) > 4:
                        break
                i += 1

            if len(divisors) == 4:
                res += sum(divisors)

        return res