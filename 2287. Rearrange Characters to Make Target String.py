class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(target)

        return min(s_counter[ch] // value for ch, value in t_counter.items())