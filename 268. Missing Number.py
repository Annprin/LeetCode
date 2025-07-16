class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        
        n = len(nums)
        need_sum = n * (n + 1) // 2
        return need_sum - sum