class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ans = [0] * 26

        for ch in set(s):
            i = s.index(ch)
            j = s.index(ch, i + 1)

            if distance[ord(ch) - 97] != j - i - 1:
                return False

        return True
