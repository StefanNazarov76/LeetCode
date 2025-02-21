class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        ans = []

        for i in range(len(sentence)):
            word = str(sentence[i])

            if word[0] in 'aeiouAEIOU':
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (i + 1)

            ans.append(word)
        return ' '.join(ans)
