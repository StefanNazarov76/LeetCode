class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct_strings = [i for i in arr if counter[i] == 1]

        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ''
