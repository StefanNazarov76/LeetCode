class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        ans = ''
        sorted_s = sorted(freq)
        reverse_s = sorted_s[::-1]

        while len(ans) < len(s):
            for ch in sorted_s:
                if freq[ch] > 0:
                    freq[ch] -= 1
                    ans += ch

            for ch in reverse_s:
                if freq[ch] > 0:
                    freq[ch] -= 1
                    ans += ch

        return ans
