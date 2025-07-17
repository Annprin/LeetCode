# time - O(n), place - O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        last_zero = -1
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l = last_zero + 1
                last_zero = i
            max_length = max(max_length, i - l)

        return max_length