class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: x[1], reverse=True)
        ans = sorted(indexed[:k], key=lambda x: x[0])

        return [x[1] for x in ans]
