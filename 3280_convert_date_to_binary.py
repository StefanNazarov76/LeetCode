class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        return '-'.join(bin(int(d))[2:] for d in date)
