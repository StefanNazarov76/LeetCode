class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_cnt = 0
        pos_cnt = 0

        for n in nums:
            if n < 0:
                neg_cnt += 1
            elif n > 0:
                pos_cnt += 1

        return max(neg_cnt, pos_cnt)
