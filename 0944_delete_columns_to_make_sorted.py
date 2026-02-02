class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        for i in range(len(strs[0])):
            temp = []

            for s in strs:
                temp.append(s[i])

            if temp != sorted(temp):
                ans += 1

        return ans
