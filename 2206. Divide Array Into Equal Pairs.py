class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for freq in counter.values():
            if freq % 2 != 0:
                return False

        return True
