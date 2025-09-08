class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)

        odd = max(freq for freq in counter.values() if freq % 2 == 1)
        even = min(freq for freq in counter.values() if freq % 2 == 0)

        return odd - even
