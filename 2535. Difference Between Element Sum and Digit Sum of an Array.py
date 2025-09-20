class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for n in nums:
            while n:
                digit_sum += n % 10
                n //= 10

        return element_sum - digit_sum
