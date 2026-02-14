class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])

        for w in words[1:]:
            c2 = Counter(w)

            c = c & c2

        return [ch for ch, freq in c.items() for _ in range(freq)]
