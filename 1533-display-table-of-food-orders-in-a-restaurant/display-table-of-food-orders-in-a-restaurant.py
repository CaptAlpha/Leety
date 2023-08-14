class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        dic = {}
        menu = set()
        for order in orders:
            menu.add(order[2])

        for order in orders:
            dic[order[1]] = ["0"]*len(menu)
        
        menuTable = {}

        menu = list(menu)
        menu.sort()

        for i, j in enumerate((menu)):
            menuTable[j] = i
        
        for order in orders:
            dic[order[1]][menuTable[order[2]]] = str(int(dic[order[1]][menuTable[order[2]]])+1)

        tableNums = (dic.keys())
        tableNums = list(tableNums)
        tableNums.sort()

        tables = [int(i) for i in tableNums]
        tables.sort()
        tableNums = tables
        newDic = {}

        for i in tableNums:
            newDic[str(i)] = dic[str(i)]

        res = ['Table']
        res.extend(list(menuTable.keys()))

        ans = [res]


        for i, j in newDic.items():
            arr = [i]
            arr.extend(j)
            ans.append(arr)


        print(menuTable, ans)

        return ans