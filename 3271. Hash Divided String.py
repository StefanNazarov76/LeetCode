class Solution:
    def stringHash(self, s: str, k: int) -> str:
        substrings = [s[i:i + k] for i in range(0, len(s), k)]

        result = ''
        for substring in substrings:
            hash_sum = sum(ord(c) - ord('a') for c in substring)
            hash_char = chr(ord('a') + (hash_sum % 26))

            result += hash_char

        return result
