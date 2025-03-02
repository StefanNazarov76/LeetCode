class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ans = 0

        current = current.split(':')
        correct = correct.split(':')
        diff = (int(correct[0]) * 60 + int(correct[1])) - (int(current[0]) * 60 + int(current[1]))

        while diff:
            print(diff)
            if diff >= 60:
                diff -= 60
            elif diff >= 15:
                diff -= 15
            elif diff >= 5:
                diff -= 5
            else:
                diff -= 1

            ans += 1

        return ans
