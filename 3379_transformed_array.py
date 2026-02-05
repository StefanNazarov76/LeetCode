class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            target = (i + nums[i]) % n
            result.append(nums[target])

        return result
