class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        if len(dict2) < len(dict1):
            dict1, dict2 = dict2, dict1
        intersect = []
        for key, count in dict1.items():
            if key in dict2:
                intersect.extend(key for i in range(min(count, dict2[key])))
        return intersect