class Solution:
    def hasSameDigits(self, s: str) -> bool:
        ans = [int(d) for d in s]

        while len(ans) > 2:
            temp = []
            for i in range(len(ans) - 1):
                temp.append((ans[i] + ans[i+1]) % 10)
            ans = temp
        return ans[0] == ans[1]
