class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(ops, a, b):
            if ops == "+": return b + a
            if ops == "-": return b-a
            if ops == "*": return b*a
            if ops == "/": return int(b/a)
        
        st = []
        opsArr = ['+', '-', '*', '/']
        for i in tokens:
            # print(f"Stack is {st}, i is {i}")
            if i not in opsArr:
                st.append(int(i))
            else:
                a = st.pop()
                b = st.pop()
                st.append(op(i, a, b))
            # print(f"After ops: Stack is {st}") 
            
        return st[-1]