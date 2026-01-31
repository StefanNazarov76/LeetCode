class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in sorted(set(letters)):
            if l > target:
                return l
        else:
            return letters[0]
