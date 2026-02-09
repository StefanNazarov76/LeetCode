class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set()
        for bin_str in nums:
            seen.add(int(bin_str, 2))

        for i in range(2 ** n):
            if i not in seen:
                return bin(i)[2:].zfill(n)
