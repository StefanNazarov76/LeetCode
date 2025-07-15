class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        ch = sentence[0][-1]

        for i in range(1, len(sentence)):
            if sentence[i][0] != ch:
                return False
            ch = sentence[i][-1]

        if sentence[0][0] != sentence[-1][-1]:
            return False

        return True
