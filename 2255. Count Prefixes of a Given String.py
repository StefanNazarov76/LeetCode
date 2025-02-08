class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        len_s = len(s)
        for word in words:
            if s[0:len(word)] == word:
                res += 1
        return res