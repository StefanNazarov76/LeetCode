class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        count = 0

        def dfs(i, current_or):
            nonlocal count
            if i == len(nums):
                if current_or == max_or:
                    count += 1
                return
            dfs(i + 1, current_or | nums[i])
            dfs(i + 1, current_or)

        dfs(0, 0)
        return count
