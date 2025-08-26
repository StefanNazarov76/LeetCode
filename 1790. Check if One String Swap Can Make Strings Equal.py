class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False

        mismatches = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(mismatches) == 0 or len(mismatches) == 2:
            return True
        else:
            return False
