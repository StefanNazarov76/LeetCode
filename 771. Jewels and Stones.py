class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0

        for jw in jewels:
            ans += stones.count(jw)

        return ans
