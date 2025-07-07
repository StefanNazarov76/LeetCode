class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counter = 0

        for i in range(len(nums)):
            if target.startswith(nums[i]):
                for j in range(len(nums)):
                    if i != j and nums[i] + nums[j] == target:
                        counter += 1

        return counter
