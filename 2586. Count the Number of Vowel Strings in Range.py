class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        counter = 0

        for w in words[left:right + 1]:
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                counter += 1

        return counter
