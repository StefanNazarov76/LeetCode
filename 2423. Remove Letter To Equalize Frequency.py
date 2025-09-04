class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)

        for ch in count:
            count[ch] -= 1

            freq = [v for v in count.values() if v > 0]
            if len(set(freq)) == 1:
                return True
            count[ch] += 1

        return False
