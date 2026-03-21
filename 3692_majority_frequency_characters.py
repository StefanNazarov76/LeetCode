class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = Counter(s)
        groups = defaultdict(list)

        for ch, freq in counter.items():
            groups[freq].append(ch)

        best_size = best_freq = 0
        ans = []

        for freq, chars in groups.items():
            if best_size < len(chars) or (best_size == len(chars) and best_freq < freq):
                best_size = len(chars)
                best_freq = freq
                ans = chars

        return ''.join(ans)
