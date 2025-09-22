class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_el = float('-inf')
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
