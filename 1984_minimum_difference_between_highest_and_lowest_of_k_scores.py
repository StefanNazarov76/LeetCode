class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        nums.sort()
        n = len(nums)

        min_diff = nums[k - 1] - nums[0]

        for i in range(1, n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff
