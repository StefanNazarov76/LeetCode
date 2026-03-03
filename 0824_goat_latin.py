class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()

        for i in range(len(words)):
            w = words[i]

            if w[0] not in 'aeiouAEIOU':
                w = w[1:] + w[0]

            w += 'ma'
            w += 'a' * (i + 1)
            words[i] = w

        return ' '.join(words)
