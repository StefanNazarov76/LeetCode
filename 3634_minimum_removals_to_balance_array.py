class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = left = 0
        n = len(nums)

        for right, num in enumerate(nums):
            while nums[right] > nums[left] * k:
                left += 1

            ans = max(ans, right - left + 1)

        return n - ans
