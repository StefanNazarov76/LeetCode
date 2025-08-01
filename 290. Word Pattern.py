class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def encode(seq):
            mapping = {}
            next_code = ord('a')
            res = ''

            for item in seq:
                if item not in mapping:
                    mapping[item] = chr(next_code)
                    next_code += 1
                res += mapping[item]

            return res

        return encode(pattern) == encode(s.split())
