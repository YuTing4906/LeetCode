class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):      # 第二輪從第二個元素往後加即可
                 result = nums[i] + nums[j]
                 if result == target:
                    return [i, j]
