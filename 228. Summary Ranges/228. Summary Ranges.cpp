class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int start=0, k=0;
        vector<string> res;
        int n = nums.size();
        string ans;
        if (n > 0) {
            ans = to_string(nums[0]);
        }
        for (int i=1; i<n; ++i) {
            if (nums[i] == nums[i-1] + 1) {
                ++k;
            } else {
                if (k > 0) {
                    ans += "->" + to_string(nums[start + k]);
                }
                res.push_back(ans);
                start = i;
                k=0;
                ans = to_string(nums[i]);
            }
        }
        if (n > 0) {
            if (k > 0) {
                ans += "->" + to_string(nums[start + k]);
            }
            res.push_back(ans);
        }
        return res;
    }
};