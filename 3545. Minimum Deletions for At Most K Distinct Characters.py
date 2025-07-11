class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        freqs = [c for _, c in counter.most_common()]

        ans = 0
        while len(freqs) > k:
            ans += freqs.pop()

        return ans
