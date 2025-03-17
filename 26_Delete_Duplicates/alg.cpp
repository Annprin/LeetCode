#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 1, last;
        if (nums.size() > 0)
            last = nums[0];
        for (int ind = 1; ind < nums.size(); ++ind){
            if (nums[ind] != last){
                nums[i] = nums[ind];
                last = nums[ind];
                ++i;
            }
        }
        return i;
    }
};