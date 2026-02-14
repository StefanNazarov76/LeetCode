class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(1 for p in words if s.startswith(p))
