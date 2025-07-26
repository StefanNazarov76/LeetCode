class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)

        for i, w in enumerate(words):
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        ans = []
        for start, end in queries:
            ans.append(prefix[end + 1] - prefix[start])

        return ans
