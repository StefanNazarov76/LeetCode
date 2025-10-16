class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        merged = [0] * (n + m)

        for i in range(m):
            merged[i] = nums1[i]

        for j in range(n):
            merged[m + j] = nums2[j]

        merged.sort()

        for i in range(m):
            nums1[i] = merged[i]

        for j in range(n):
            nums1[j + m] = merged[j + m]
