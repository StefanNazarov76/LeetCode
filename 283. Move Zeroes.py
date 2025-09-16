class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = 0
        left = 0

        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                right += 1
                left += 1
            else:
                right += 1

        while left < n:
            nums[left] = 0
            left += 1

        return
