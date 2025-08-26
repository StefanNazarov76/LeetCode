class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set([int(ch) for ch in s if ch.isdigit()])

        if len(digits) > 1:
            return sorted(digits)[-2]
        else:
            return -1
