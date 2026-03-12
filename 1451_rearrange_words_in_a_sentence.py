class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text = sorted(text, key=len)
        text = ' '.join(text)
        text = text[0].upper() + text[1:].lower()
        return text
