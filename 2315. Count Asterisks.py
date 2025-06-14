class Solution:
    def countAsterisks(self, s: str) -> int:
        parts = s.split('|')
        joined_parts = ''.join(parts[i] for i in range(0, len(parts), 2))

        return joined_parts.count('*')
