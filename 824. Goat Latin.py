class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []

        for i, w in enumerate(sentence.split()):
            if w[0] in 'aeiouAEIOU':
                w = w + 'ma'
            else:
                w = w[1:] + w[:1] + 'ma'

            w += 'a' * (i + 1)

            ans.append(w)

        return ' '.join(ans)
