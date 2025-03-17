#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i, j = size(nums) - 1;
        for (i = 0; i <= j; ++i){
            if (nums[i] == val){
                while(j>=0 && nums[j] == val)
                    --j;
                if (j < i)
                    break;
                nums[i] = nums[j];
                --j;
            }
        }
        return i;
    }
};