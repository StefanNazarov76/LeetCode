class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for index, letter in enumerate(s):
            ans += (index + 1) * (123 - ord(letter))

        return ans