class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxlen=0, len=0, len1=0, len2=0;
        for (int i=0; i<n; ++i) {
            if (nums[i] > 0) {
                ++len1;
            } else {
                maxlen = maxlen < len1 + len2 ? len1 + len2 : maxlen;
                len2 = len1;
                len1 = 0;
            }
        }
        maxlen = maxlen < len1 + len2 ? len1 + len2 : maxlen;
        maxlen = maxlen == n ? n - 1 : maxlen;
        return maxlen;
    }
};