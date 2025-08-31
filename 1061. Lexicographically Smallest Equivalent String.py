class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(97 + i): chr(97 + i) for i in range(26)}
        size = [1] * 26

        def find(z):
            while z != parent[z]:
                parent[z] = parent[parent[z]]
                z = parent[z]
            return z

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if size[ord(root_x) - 97] <= size[ord(root_y) - 97]:
                    if ord(root_x) < ord(root_y):
                        parent[root_y] = root_x
                        size[ord(root_x) - 97] += size[ord(root_y) - 97]
                    else:
                        parent[root_x] = root_y
                        size[ord(root_y) - 97] += size[ord(root_x) - 97]


                elif size[ord(root_x) - 97] > size[ord(root_y) - 97]:
                    if ord(root_x) < ord(root_y):
                        parent[root_y] = root_x
                        size[ord(root_x) - 97] += size[ord(root_y) - 97]

                    else:
                        parent[root_x] = root_y
                        size[ord(root_y) - 97] += size[ord(root_x) - 97]

        n = len(s1)

        for i in range(n):
            union(s1[i], s2[i])

        ans = ''

        for ch in baseStr:
            ans += find(ch)

        return ans
