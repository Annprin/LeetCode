#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        int n = nums.size();
        for (int i=0; i<n; ++i) {
            int key = target - nums[i];
            if (m[key] > 0) {
                return {m[key]-1, i};
            } else {
                m[nums[i]] = i + 1;
            }
        }
    }
};