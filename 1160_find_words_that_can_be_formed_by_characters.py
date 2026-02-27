class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0

        for w in words:
            if Counter(w) <= chars:
                ans += len(w)

        return ans
