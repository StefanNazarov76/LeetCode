class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = ''

        for ch in order:
            curr = ch * counter[ch]
            ans += curr

        for ch in counter:
            if ch not in order:
                ans += ch * counter[ch]

        return ans
