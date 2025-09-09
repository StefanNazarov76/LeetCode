class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()

        if not words:
            return '#'

        ans = '#' + words[0].lower()

        for word in words[1:]:
            ans += word.capitalize()

        return ans[:100]
