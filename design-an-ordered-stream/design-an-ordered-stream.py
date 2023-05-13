class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1


    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if self.ptr == idKey:
            chunk = []
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
            return chunk
        else:
            return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)