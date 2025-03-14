class Solution:
    def sortString(self, s: str) -> str:
        char_count = Counter(s)
        ans = []

        unique_chars = sorted(char_count.keys())

        while len(ans) < len(s):
            for ch in unique_chars:
                if char_count[ch] > 0:
                    ans.append(ch)
                    char_count[ch] -= 1

            for ch in reversed(unique_chars):
                if char_count[ch] > 0:
                    ans.append(ch)
                    char_count[ch] -= 1

        return ''.join(ans)