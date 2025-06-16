class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = -1
        for i, num in enumerate(nums):
            if num != 0 and zero != -1:
                nums[zero] = num
                nums[i] = 0
                zero += 1
            elif num == 0 and zero < 0:
                zero = i