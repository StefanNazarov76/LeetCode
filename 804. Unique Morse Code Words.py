class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_table = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                       "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                       "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                       "y": "-.--", "z": "--.."}

        transformed = set()
        for w in words:
            code = ''.join(morse_table[c] for c in w)
            transformed.add(code)

        return len(transformed)