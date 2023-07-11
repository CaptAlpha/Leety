class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        people = set()
        for (u,v) in trust:
            graph[u].append(v)
            people.add(u)
            people.add(v)
        
        
        judges = []
        judge = -1
        for i, j in graph.items():
            if len(j) == 0:
                judges.append(i)
        check = 0
        print(graph)
        for person in judges:
            
            for i,j in graph.items():
                if person not in j and i != person:
                    check = 1
            if check==0:
                return person
        return -1




