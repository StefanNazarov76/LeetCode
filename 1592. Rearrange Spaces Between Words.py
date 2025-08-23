class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(" ")
        words = text.split()

        if len(words) > 1:
            space_btwn_words = ' ' * (total_spaces // (len(words) - 1))
            extra_spaces = ' ' * (total_spaces % (len(words) - 1))

            return space_btwn_words.join(words) + extra_spaces

        else:
            return words[0] + (' ' * total_spaces if words else '')
