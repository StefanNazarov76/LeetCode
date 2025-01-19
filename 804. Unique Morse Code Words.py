class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mors = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        trans = []

        for w in words:
            curr = ''

            for ch in w:
                curr += mors[ord(ch) - 97]

            trans.append(curr)

        return len(set(trans))
