class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n, ans = len(nums), 0
        pre = [0 for _ in range(n)]
        suff = [0 for _ in range(n)]

        for i in range(n):
            if i: pre[i] = pre[i - 1]
            if nums[i]: pre[i] += 1
            else: pre[i] = 0
            ans = max(ans, pre[i])

        for i in range(n -1, -1, -1):
            if i < n - 1: suff[i] = suff[i + 1]
            if nums[i]: suff[i] += 1
            else: suff[i] = 0
            
        for i in range(n):
            if nums[i]: continue
            res = 0
            if i > 0: res += pre[i - 1]
            if i < n - 1: res += suff[i + 1]
            ans = max(ans, res + 1)
        return ans