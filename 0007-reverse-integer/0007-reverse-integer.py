class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2 ** 31 -1, -2 ** 31
        num, rev_num = abs(x), 0
        while num>0:
            rem = num%10
            rev_num = rev_num * 10 + rem
            num=num//10

        if x<0:
            rev_num = -rev_num
        if rev_num > MAX_INT or rev_num < MIN_INT:
            return 0
        return rev_num
        