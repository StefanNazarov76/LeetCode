class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        max_chairs = 0

        for i in s:
            if i == 'E':
                chairs += 1
            else:
                chairs -= 1

            max_chairs = max(chairs, max_chairs)

        return max_chairs
