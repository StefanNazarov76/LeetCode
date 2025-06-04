class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')

        year = bin(int(year))
        month = bin(int(month))
        day = bin(int(day))

        return f"{year[2:]}-{month[2:]}-{day[2:]}"
