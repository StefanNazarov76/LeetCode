class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        words_map = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                     'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
                     'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                     'y': "-.--", 'z': "--.."}
        ans = set()

        for w in words:
            transformed = ''

            for ch in w:
                transformed += words_map[ch]

            ans.add(transformed)
        return len(ans)
