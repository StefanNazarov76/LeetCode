class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def convert_to_days(date):
            days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

            month, day = [int(i) for i in date.split('-')]
            return days[month - 1] + day

        arr_Al = convert_to_days(arriveAlice)
        leave_Al = convert_to_days(leaveAlice)
        arr_Bob = convert_to_days(arriveBob)
        leave_Bob = convert_to_days(leaveBob)

        ans = min(leave_Al, leave_Bob) - max(arr_Al, arr_Bob)
        ans = 0 if ans < 0 else ans + 1

        return ans
