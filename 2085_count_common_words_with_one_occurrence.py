class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        ans = 0

        for word, freq in counter1.items():
            if freq == 1 and counter2[word] == 1:
                ans += 1

        return ans
