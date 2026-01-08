class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = 0
        consonant = 0

        for letter, freq in Counter(s).most_common():
            if letter in 'aeiou' and vowel == 0:
                vowel = freq
            elif letter not in 'aeiou' and consonant == 0:
                consonant = freq

            if vowel != 0 and consonant != 0:
                break

        return vowel + consonant
