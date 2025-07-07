class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        ans = ''
        for ch, freq in counter.most_common():
            ans += ch * freq

        return ans
