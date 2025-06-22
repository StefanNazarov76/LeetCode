class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ = s.count(s[0])

        for i in set(s):
            if s.count(i) != occ:
                return False

        return True
