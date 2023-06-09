class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters1 = sorted(letters)

        for i in range(len(letters1)):
            if(letters1[i]>target):
                return letters1[i]

        return letters[0]

