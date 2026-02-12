class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 + (c % 2 == 0) for c in Counter(s).values())
