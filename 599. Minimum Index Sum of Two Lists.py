class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        min_idx = sys.maxsize
        ans = []

        for idx, word in enumerate(list2):
            index_map[word] = idx

        for idx, word in enumerate(list1):
            if word in index_map:
                total_idx = index_map[word] + idx

                if total_idx < min_idx:
                    min_idx = total_idx
                    ans = [word]

                elif total_idx == min_idx:
                    ans.append(word)

        return ans
