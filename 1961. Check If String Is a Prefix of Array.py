class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ''

        for word in words:
            temp += word

            if len(temp) > len(s):
                return False

            if temp == s:
                return True

        return False
