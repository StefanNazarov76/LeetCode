class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        res = 1

        for i in nums:
            if i < 0:
                res *= -1

        return 1 if res > 0 else -1
