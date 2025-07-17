class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word):
            mapping = {}
            next_ch = 0

            res = []
            for ch in word:
                if ch not in mapping:
                    mapping[ch] = str(next_ch)
                    next_ch += 1

                res.append(mapping[ch])

            return ' '.join(res)

        pattern = encode(pattern)
        return [w for w in words if encode(w) == pattern]
