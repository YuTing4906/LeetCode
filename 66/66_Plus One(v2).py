class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        result = ''                # 用來暫存資料
        for i in  digits:
            result += str(i)       # 將list中的元素串在一起
        result = int(result) + 1
        digits = list(str(result))
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits
        
        """
        # 簡寫版本
        digits = list(str(int(''.join(str(i) for i in digits)) + 1))
        return [int(digit) for digit in digits]
        """
