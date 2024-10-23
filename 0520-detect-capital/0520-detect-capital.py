class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower, upper = 0, 0
        for i in word:
            if 96 < ord(i) < 123:
                lower+=1
            elif 64 < ord(i) < 91:
                upper+=1
            else:
                pass
        l = len(word)
        if l == lower or l == upper:
            return True
        elif 64 < ord(word[0]) < 91 and upper == 1:
            return True
        else:
            return False

        