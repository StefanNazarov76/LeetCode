class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0

        paper_time = 0
        for i, g in enumerate(garbage):
            if i - 1 >= 0:
                paper_time += travel[i - 1]

            if 'P' in g:
                paper_time += g.count('P')
                time += paper_time
                paper_time = 0

        glass_time = 0
        for i, g in enumerate(garbage):
            if i - 1 >= 0:
                glass_time += travel[i - 1]

            if 'G' in g:
                glass_time += g.count('G')
                time += glass_time
                glass_time = 0

        metal_time = 0
        for i, g in enumerate(garbage):
            if i - 1 >= 0:
                metal_time += travel[i - 1]

            if 'M' in g:
                metal_time += g.count('M')
                time += metal_time
                metal_time = 0

        return time
