class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)

        def generate(s):
            if len(s) == len(nums):
                if s not in seen:
                    return s
                return None

            res = generate(s + '0')
            if res:
                return res
            return generate(s + '1')

        return generate('')
