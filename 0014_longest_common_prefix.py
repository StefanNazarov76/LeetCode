class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for i in range(len(strs[0])):
            temp = strs[0][:i + 1]

            for word in strs:
                if not word.startswith(temp):
                    return prefix

            prefix = temp

        return prefix
