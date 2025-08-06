class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = Counter()

        for i in licensePlate.lower():
            if i.isalpha():
                counter[i] += 1

        words = sorted(words, key=len)

        for w in words:
            if counter <= Counter(w.lower()):
                return w
