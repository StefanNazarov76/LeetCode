class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        o = s.split("0")
        o = max(o)

        z = s.split("1")
        z = max(z)

        return len(o) > len(z)
