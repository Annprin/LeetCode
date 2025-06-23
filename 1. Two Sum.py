class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        for i, num in enumerate(nums):
            if target - num in vals:
                return [i, vals[target - num]]
            else:
                vals[num] = i
        return -1