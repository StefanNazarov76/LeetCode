class Solution:
    def dayOfYear(self, date: str) -> int:
        month_sum = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        year, month, day = [int(i) for i in date.split('-')]

        if year % 4 == 0 and year != 1900 and month > 2:
            day += 1

        return month_sum[month - 1] + day
