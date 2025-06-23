class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, 0
        for bit in nums:
            if bit == 0:
                k -= 1
            end += 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
        return end - start