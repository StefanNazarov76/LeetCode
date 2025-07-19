class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        counter = 0

        for i in range(len(word)):
            if word[i] not in vowels:
                continue

            unique = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break

                unique.add(word[j])

                if len(unique) == 5:
                    counter += 1

        return counter
