class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if list(set(s)) != list(set(goal)):
            return False

        n = len(s)

        arr = []

        for i in range(0, len(s)):
            if s[i]!=goal[i]:
                arr.append(i)


        if len(arr) == 0:
            array = []

            for i in s:
                if i not in array:
                    array.append(i)
                else:
                    return True

            return False


        li = list(s)


        li[arr[0]], li[arr[1]] = li[arr[1]], li[arr[0]]

        s= ""
        for i in li: s+=i

        if s == goal:
            return True

        return False
        
