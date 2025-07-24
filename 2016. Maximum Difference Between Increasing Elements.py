class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        low = nums[0]

        for i in range(1, n):
            if low < nums[i]:
                temp = nums[i] - low
                ans = max(ans, temp)

            low = min(low, nums[i])

        return ans
