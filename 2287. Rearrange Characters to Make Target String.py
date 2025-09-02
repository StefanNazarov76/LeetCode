class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = Counter(s)
        t = Counter(target)

        return min(s[ch] // t[ch] for ch in target)
