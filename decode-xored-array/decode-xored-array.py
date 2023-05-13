class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        li = []
        li.append(first)
        for i in range(len(encoded)):
            li.append(abs(li[i]^encoded[i]))

        return li