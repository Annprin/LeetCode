class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0:1}
        all_sum, count = 0, 0
        for val in nums:
            all_sum += val
            if (all_sum - k in sums):
                count += sums[all_sum - k]
            if (all_sum in sums):
                sums[all_sum] += 1
            else:
                sums[all_sum] = 1
        return count