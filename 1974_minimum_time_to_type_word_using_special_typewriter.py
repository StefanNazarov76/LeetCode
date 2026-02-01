class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        position = 'a'

        for ch in word:
            total_time += min(abs(ord(ch) - ord(position)), 26 - abs(ord(ch) - ord(position)))
            total_time += 1
            position = ch

        return total_time
