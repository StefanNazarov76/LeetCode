class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        s = s.replace('-', '').upper()
        first_group_len = len(s) % k

        if first_group_len:
            ans.append(s[:first_group_len])

        for i in range(first_group_len, len(s), k):
            ans.append(s[i:i + k])

        return '-'.join(ans)