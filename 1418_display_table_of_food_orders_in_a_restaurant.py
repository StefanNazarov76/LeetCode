class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = set()
        foods = set()
        count = {}

        for _, table, food in orders:
            tables.add(table)
            foods.add(food)

            if table not in count:
                count[table] = {}
            if food not in count[table]:
                count[table][food] = 0

            count[table][food] += 1

        tables = sorted(tables, key=int)
        foods = sorted(foods)

        ans = [['Table', *foods]]

        for table in tables:
            row = [table] + ['0'] * len(foods)

            for food, cnt in count.get(table, {}).items():
                j = foods.index(food)
                row[j + 1] = str(cnt)

            ans.append(row)

        return ans
