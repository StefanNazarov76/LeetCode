class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num in nums[i+1:]:
                return num
