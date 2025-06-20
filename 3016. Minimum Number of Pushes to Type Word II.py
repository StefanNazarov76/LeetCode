class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        pos = 0

        freq_map = Counter(word)
        for ch, freq in freq_map.most_common():
            total += freq * ((pos // 8) + 1)
            pos += 1

        return total