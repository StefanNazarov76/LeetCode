class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last_num = 0

        for token in s.split():
            if token.isdigit():
                if int(token) > last_num:
                    last_num = int(token)
                else:
                    return False

        return True
