class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for ch in strs[0]:
            prefix += ch

            for s in strs[1:]:
                if not s.startswith(prefix):
                    return prefix[:-1]

        return prefix
