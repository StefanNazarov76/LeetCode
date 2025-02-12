class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = {}
        for word in words1:
            if word not in dict1:
                dict1[word] = 0
            dict1[word] += 1

        dict2 = {}
        for word in words2:
            if word not in dict2:
                dict2[word] = 0
            dict2[word] += 1

        ans = 0
        for w in dict1.keys():
            if w in dict2.keys() and dict1[w] == 1 and dict2[w] == 1:
                ans += 1

        return ans