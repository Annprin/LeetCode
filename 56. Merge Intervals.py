class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        prev_left, prev_right = intervals[0]
        ans = []
        
        for left, right in intervals[1:]:
            if left <= prev_right:
                prev_right = max(prev_right, right)
            else:
                ans.append([prev_left, prev_right])
                prev_left, prev_right = left, right
        ans.append([prev_left, prev_right])
        return ans