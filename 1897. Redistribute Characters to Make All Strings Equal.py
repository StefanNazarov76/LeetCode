class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}

        for word in words:
            for char in word:
                if char not in d:
                    d[char] = 0
                d[char] += 1

        for char in d:
            if d[char] % len(words) != 0:
                return False

        return True
