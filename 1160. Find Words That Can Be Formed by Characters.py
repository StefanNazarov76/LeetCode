class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)

        ans = 0
        for w in words:
            for ch in set(w):
                if w.count(ch) > chars.count(ch):
                    break
            else:
                ans += len(w)

        return ans
