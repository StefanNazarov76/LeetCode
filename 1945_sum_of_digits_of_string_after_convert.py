class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ''
        ans = ''

        for ch in s:
            ans += str(ord(ch) - 96)

        for _ in range(k):
            temp = 0

            for d in ans:
                temp += int(d)

            ans = str(temp)

        return int(ans)
