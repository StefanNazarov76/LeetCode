class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum(f for f in (Counter(t) - Counter(s)).values())
