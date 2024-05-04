class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):    # 從最後一個數字依序往前檢查
            digits[i] += 1
            if digits[i] == 10:
                carry = True
                digits[i] = 0
            else:
                carry = False
                break
        if carry == True:       # for迴圈跑完，還有進位的話，第一個數字為9
            return [1] + digits
        else:
            return digits