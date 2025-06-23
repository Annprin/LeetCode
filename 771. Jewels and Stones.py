class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewSet = set(jewels)

        count = 0
        for c in stones:
            if c in jewSet:
                count += 1
        return count