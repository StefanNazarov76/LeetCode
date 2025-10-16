class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num, _ = min(Counter(nums).items(), key=lambda x: x[1])
        return num
