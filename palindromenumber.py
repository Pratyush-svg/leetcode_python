class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        b = 0
        if(x < 0):
            return False
        else:
            while(a != 0):
                b = (b*10)+a % 10
                a = a//10
        if(x == b):
            return True
        else:
            return False
