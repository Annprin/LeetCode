# time - O(n), space - O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        while r < len(chars):
            letter = chars[r]
            count = 0
            while r < len(chars) and chars[r] == letter:
                r += 1
                count += 1
            chars[l] = letter
            l += 1
            if count > 1:
                for c in str(count):
                    chars[l] = c
                    l += 1
        return l