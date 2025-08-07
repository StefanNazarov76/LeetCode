class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        skip = 0
        ans = ''

        for i in range(0, len(s), k):
            if skip % 2 == 0:
                ans += s[i:i + k][::-1]
            else:
                ans += s[i:i + k]

            skip += 1

        return ans
