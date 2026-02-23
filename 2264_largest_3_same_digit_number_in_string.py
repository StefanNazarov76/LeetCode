class Solution:
    def largestGoodInteger(self, num: str) -> str:
        numbers = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']

        for n in numbers:
            if n in num:
                return n

        return ''
