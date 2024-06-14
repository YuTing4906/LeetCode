class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_x = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        reversed_x *= sign
        if reversed_x > 2 ** 31 -1 or reversed_x < -(2 ** 31):
            return 0
        return reversed_x