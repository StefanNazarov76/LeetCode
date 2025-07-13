class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(0, 26):
            letter = chr(ord('a') + i)

            if letter in s:
                first = s.find(letter)
                second = s.find(letter, first + 1)

                if distance[i] != abs(second - first) - 1:
                    return False

        return True
