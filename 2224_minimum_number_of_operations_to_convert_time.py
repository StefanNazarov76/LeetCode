class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def toMins(time):
            time = time.split(':')
            return int(time[1]) + int(time[0]) * 60

        diff = toMins(correct) - toMins(current)
        ans = 0

        ans += diff // 60
        diff = diff % 60

        ans += diff // 15
        diff = diff % 15

        ans += diff // 5
        diff = diff % 5

        ans += diff // 1
        diff = diff % 1

        return ans
