class Solution:
    def finalString(self, s: str) -> str:
        curr_str = ''

        for ch in s:
            if ch == 'i':
                curr_str = curr_str[::-1]
            else:
                curr_str += ch

        return curr_str
    