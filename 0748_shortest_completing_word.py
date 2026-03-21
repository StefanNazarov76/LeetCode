class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = ''

        for ch in licensePlate:
            if ch.isalpha():
                letters += ch.lower()

        counter = Counter(letters)
        words = sorted(words, key=len)

        for w in words:
            if counter <= Counter(w):
                return w
