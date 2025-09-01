class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(word):
            hyphens = 0
            punctu = 0

            for i, c in enumerate(word):
                if c.isdigit():
                    return False

                if c == '-':
                    hyphens += 1
                    if (
                            hyphens > 1
                            or i == 0
                            or i == len(word) - 1
                            or not word[i - 1].isalpha()
                            or not word[i + 1].isalpha()
                    ):
                        return False

                if c in '!.,':
                    punctu += 1
                    if punctu > 1 or i != len(word) - 1:
                        return False

            return True

        ans = 0
        for w in sentence.split():
            if is_valid(w):
                ans += 1

        return ans

