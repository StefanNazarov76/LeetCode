class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        curr = ord('a')

        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(curr)
                curr += 1

        return ''.join([mapping[ch] if ch != ' ' else ch for ch in message])
