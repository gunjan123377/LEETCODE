class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        flag = [0]*len(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    flag[stack.pop()] = 1
                    flag[i] = 1
            else:
                continue
        ans = ""
        for i, c in enumerate(s):
            if c in "()":
                if flag[i]:
                    ans+=c
                else:
                    continue
            else:
                ans+=c
        return ans