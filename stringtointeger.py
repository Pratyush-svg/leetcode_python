# leetcode8 string to integer(atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) < 1:
            return 0
        s = s.lstrip()
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        isPositive = len(s) > 1 and s[0] == '+'
        isNegative = len(s) > 1 and s[0] == '-'
        i = 0
        number = 0
        if isPositive or isNegative:
            i = 1
        else:
            i = 0
        while i < len(s) and '0' <= s[i] <= '9':
            number = number*10+(ord(s[i])-ord('0'))
            i = i+1
        if isNegative:
            number = -number
        else:
            number = number

        if number < INT_MIN:
            return INT_MIN
        elif number > INT_MAX:
            return INT_MAX
        else:
            return number
