class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pos1, pos2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if pos1 < 0 or (pos2 >= 0 and nums1[pos1] < nums2[pos2]):
                nums1[i] = nums2[pos2]
                pos2 -= 1
            else:
                nums1[i] = nums1[pos1]
                pos1 -= 1
