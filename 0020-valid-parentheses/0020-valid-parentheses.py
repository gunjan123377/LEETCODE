class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_braces = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack:
                    if pair_braces[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True


        