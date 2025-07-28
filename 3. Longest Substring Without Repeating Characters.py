class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set(s)
        max_length = 0

        for start in range(len(s)):
            end = start
            seen_chars = set()

            while end < len(s) and s[end] not in seen_chars:
                seen_chars.add(s[end])
                end += 1

            max_length = max(max_length, len(seen_chars))

            if max_length == len(unique_chars):
                return max_length

        return max_length
