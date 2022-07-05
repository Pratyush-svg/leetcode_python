# leet code 7 reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if x > 0:
            temp = x
        else:
            temp = (x*-1)
        y = 0
        while(temp > 0):
            y = y*10+(temp % 10)
            temp = temp//10

        if y > INT_MAX or y < INT_MIN:
            return 0
        elif x < 0:
            return y*-1
        else:
            return y
