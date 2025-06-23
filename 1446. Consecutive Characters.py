class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        
        power, maxPower = 1, 1
        ex = s[0]
        for char in s[1:]:
            if char == ex:
                power += 1
                maxPower = max(power, maxPower)
            else:
                power = 1
                ex = char
        return maxPower