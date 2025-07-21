class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=len)
        sentence = sentence.split()

        for i, w in enumerate(sentence):
            for r in dictionary:
                if w.startswith(r):
                    sentence[i] = r
                    break

        return ' '.join(sentence)
