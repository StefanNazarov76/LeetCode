class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convert_to_mins(time):
            hours, mins = [int(i) for i in time.split(':')]
            return hours * 60 + mins

        diff = convert_to_mins(correct) - convert_to_mins(current)
        ans = 0

        for op in [60, 15, 5, 1]:
            ans += diff // op
            diff = diff % op

        return ans
