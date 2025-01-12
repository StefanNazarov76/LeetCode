class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = [''] * len(s)

        for i in range(len(indices)):
            new_string[indices[i]] = s[i]

        return ''.join(new_string)
