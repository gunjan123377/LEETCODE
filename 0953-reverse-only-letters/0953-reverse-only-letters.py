class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s)-1
        s=list(s)

        while right> left:
            if not s[left].isalpha():
                left+=1
            elif not s[right].isalpha():
                right-=1
            else:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1

        return  "".join(s)
