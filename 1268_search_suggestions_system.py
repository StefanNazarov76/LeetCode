class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans = []

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            temp = []

            for p in products:
                if p.startswith(prefix):
                    temp.append(p)

                if len(temp) == 3:
                    break

            ans.append(temp)

        return ans
