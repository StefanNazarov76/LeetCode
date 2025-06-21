class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = set()

        for city, _ in paths:
            origins.add(city)

        for _, destination in paths:
            if destination not in origins:
                return destination
