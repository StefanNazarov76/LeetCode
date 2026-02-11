class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ans = ''

        for char, freq in counter.most_common():
            ans += char * freq

        return ans
