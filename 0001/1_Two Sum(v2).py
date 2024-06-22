class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:   
                if hash_table[target - nums[i]] != i:         # 避免出現target-num[i]=num[i]誤判的情況
                    return [hash_table[target - nums[i]], i]
            hash_table[nums[i]] = i 
