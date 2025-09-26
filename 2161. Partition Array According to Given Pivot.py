class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        r = []
        p = []

        for n in nums:
            if n < pivot:
                l.append(n)
            elif n == pivot:
                p.append(n)
            else:
                r.append(n)

        return l + p + r
