#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 1, last, count = 0;
        if (nums.size() > 0){
            last = nums[0];
            count = 1;
        }
        for (int ind = 1; ind < nums.size(); ++ind){
            if (nums[ind] != last){
                nums[i] = nums[ind];
                last = nums[ind];
                ++i;
                count = 1;
            }
            else{
                ++count;
                if (count < 3){
                    nums[i] = nums[ind];
                    ++i;
                }
            }
        }
        return i;
    }
};