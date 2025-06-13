class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split()

        for i in s.split():
            index = int(i[-1]) - 1
            word = i[:-1]

            ans[index] = word

        return ' '.join(ans)