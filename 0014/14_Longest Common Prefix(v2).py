class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        long_common = ""
        strs.sort()
        for i in range(len(min(strs, key=len))):
            if strs[0][i] != strs[-1][i]:
                return long_common
            else:
                long_common += strs[0][i]
        return long_common
