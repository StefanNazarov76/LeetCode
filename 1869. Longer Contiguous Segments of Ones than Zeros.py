class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        curr0 = 0
        max0 = 0
        curr1 = 0
        max1 = 0

        for i in s:
            if i == '0':
                curr0 += 1
                curr1 = 0
            else:
                curr1 += 1
                curr0 = 0

            max0 = max(max0, curr0)
            max1 = max(max1, curr1)

        return max1 > max0


