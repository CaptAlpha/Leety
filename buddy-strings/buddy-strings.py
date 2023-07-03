class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):  # Check if the lengths of the strings are different
            return False

        if list(set(s)) != list(set(goal)):  # Check if the set of characters in 's' is different from the set of characters in 'goal'
            return False

        n = len(s)

        arr = []

        for i in range(0, len(s)):
            if s[i] != goal[i]:  # Find indices where the characters differ between 's' and 'goal'
                arr.append(i)

        if len(arr) == 0:  # If 's' and 'goal' are the same, check if there are duplicate characters in 's'
            array = []

            for i in s:
                if i not in array:
                    array.append(i)
                else:
                    return True

            return False

        li = list(s)

        # Swap the characters at the differing indices in 's'
        li[arr[0]], li[arr[1]] = li[arr[1]], li[arr[0]]

        s = ""
        for i in li:
            s += i

        if s == goal:  # Check if 's' is equal to 'goal' after the swap
            return True

        return False
