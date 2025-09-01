class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []

        for word in title.split():
            if len(word) > 2:
                word = word[0].upper() + word[1:].lower()
            else:
                word = word.lower()

            ans.append(word)

        return ' '.join(ans)
