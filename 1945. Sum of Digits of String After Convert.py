class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(ch) - 96) for ch in s)

        for _ in range(k):
            t = sum(int(ch) for ch in s)
            s = str(t)

        return int(s)
