class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        long_common = ""

        # 找出List中最短字串的長度
        shortest_str = len(strs[0])
        for str in strs:
            if len(str) < shortest_str:
                shortest_str = len(str)
        
        for j in range(shortest_str):
            compare_char = strs[0][j]
            for i in range(1, len(strs)):
                if compare_char != strs[i][j]:
                    return long_common          
            long_common += compare_char 
        return long_common