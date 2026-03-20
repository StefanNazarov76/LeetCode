class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqs = []
        for w in words:
            counter = sorted(Counter(w).items())
            freqs.append(counter[0][1])

        ans = []
        for query in queries:
            query_freq = sorted(Counter(query).items())[0][1]
            count = 0

            for freq in freqs:
                if query_freq < freq:
                    count += 1

            ans.append(count)

        return ans
