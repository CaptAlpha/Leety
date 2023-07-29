class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        dic = {}

        for i in range(len(score)):
            dic[score[i][k]] = score[i]

        li = list(dic.keys())

        li.sort(reverse=True)

        ans = []

        for i in li:
            ans.append(dic[i])

    



        return ans