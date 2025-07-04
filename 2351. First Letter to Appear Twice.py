class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_set = set()

        for char in s:
            if char in char_set:
                return char

            char_set.add(char)
