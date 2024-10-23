class Solution:
    def calculate(self, s: str) -> int:

        stack, postfix = [], []
        operators = {"+" : 1, "-" : 1, "(" : 0, ")" : 0}

        def read(s):
            s=s.replace(" ","")
            infix, i = [], 0

            while i < len(s):
                if s[i] in operators:
                    if s[i] == "-":
                        if i==0 or (i-1>=0 and s[i-1] == "("):
                            infix.append(0)
                    infix.append(s[i])
                    i+=1
                else:
                    num = ""
                    while i < len(s) and s[i].isdigit():
                        num+=s[i]
                        i+=1
                    infix.append(num)
            return infix
                
        for c in read(s):
            if c == "(":
                stack.append(c)
            elif c == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
            elif c in operators:
                while stack and operators[stack[-1]] >= operators[c]:
                    postfix.append(stack.pop())
                stack.append(c)
            else:
                postfix.append(c)

        while stack:
            postfix.append(stack.pop())
        
        for c in postfix:
            if c not in operators:
                stack.append(int(c))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if c == "+":
                    result = n1 + n2
                elif c == "-":
                    result = n1 - n2
                stack.append(result)

        return stack[0]