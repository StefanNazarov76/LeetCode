class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoder = {}
        i = 97

        for k in key.replace(' ', ''):
            if k not in decoder:
                decoder[k] = chr(i)
                i += 1

        new_message = ''
        for i in message:
            if i == ' ':
                new_message += i
            else:
                new_message += decoder[i]

        return new_message
