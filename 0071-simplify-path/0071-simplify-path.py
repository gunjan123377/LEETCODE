class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p:
                if p == ".":
                    pass
                elif p == "..":
                    if stack:
                        stack.pop()
                    else:
                        pass
                else:
                    stack.append(p)
        return "/" + "/".join(stack)
