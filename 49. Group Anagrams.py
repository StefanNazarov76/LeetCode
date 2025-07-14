class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        keys = []

        for word in strs:
            key = sorted(word)

            found = False
            for i in range(len(keys)):
                if keys[i] == key:
                    ans[i].append(word)
                    found = True
                    break

            if not found:
                keys.append(key)
                ans.append([word])

        return ans
