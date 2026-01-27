class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d1 = set()
        d2 = set()

        for path in paths:
            d1.add(path[0])
            d2.add(path[1])

        for city in d2:
            if city not in d1:
                return city
