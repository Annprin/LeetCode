# time - O(n), place - O(n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    res.append(str(nums[start]))
                else:
                    res.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        if start == len(nums) - 1:
            res.append(str(nums[start]))
        else:
            res.append(f"{nums[start]}->{nums[-1]}")
        return res