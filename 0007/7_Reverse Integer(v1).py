class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_x = 0
        if x > 0:
            x = str(x)
            for i in range(len(x) - 1, -1, -1):    # 從最後一個數字依序往前檢查
                reverse_x += int(x[i]) * pow(10, i)
        else:
            x = str(x)
            for i in range(len(x) - 1, 0, -1):     # 從最後一個數字依序往前檢查
                reverse_x -= int(x[i]) * pow(10, i - 1)
        if reverse_x > pow(2,31)-1 or reverse_x < -pow(2,31):   
            return 0 
        return reverse_x