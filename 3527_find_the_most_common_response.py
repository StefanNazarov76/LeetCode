class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter(w for r in responses for w in set(r))
        max_freq = max(counter.values())
        return min(word for word, freq in counter.items() if freq == max_freq)
