class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans += 1

                if nums[j] + nums[i] == target:
                    ans += 1

        return ans
