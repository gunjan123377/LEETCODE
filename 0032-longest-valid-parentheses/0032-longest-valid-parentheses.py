class Solution:
    def longestValidParentheses(self, s: str) -> int:
        flag = [0]*len(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    flag[stack.pop()] = 1
                    flag[i] = 1
                else:
                    continue

        count = 0
        ans = 0
        for c in flag:
            if c:
                count+=1
            else:
                count=0
            ans = max(count, ans)
        return ans

