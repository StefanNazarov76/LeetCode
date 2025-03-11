class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        power = 1
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                power = max(power, curr)
                curr = 1

        return max(power, curr)
