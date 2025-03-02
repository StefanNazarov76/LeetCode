class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []

        for word in title.split():
            word = word.lower()

            if len(word) > 2:
                word = word[0].upper() + word[1:]

            ans.append(word)

        return ' '.join(ans)