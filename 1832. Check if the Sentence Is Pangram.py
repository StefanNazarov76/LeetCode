class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(97, 123):
            if not chr(i) in sentence:
                return False

        return True
