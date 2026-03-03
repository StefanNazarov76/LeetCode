class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = [words[0]]

        for w in words[1:]:
            if sorted(w) != sorted(stack[-1]):
                stack.append(w)

        return stack
