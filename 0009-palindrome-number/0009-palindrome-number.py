class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            actual_num = x
            con_num = 0
            while x>0:
                y = x%10
                x = x//10
                con_num = con_num*10 + y
            return actual_num == con_num
        else:
            return False



        