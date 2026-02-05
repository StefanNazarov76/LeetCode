class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalize(word):
            s = set()
            i = 0

            for ch in word:
                if ch not in s:
                    word = word.replace(ch, str(i))
                    i += 1

            return word

        ans = []
        pattern = normalize(pattern)

        for word in words:
            if normalize(word) == pattern:
                ans.append(word)

        return ans
