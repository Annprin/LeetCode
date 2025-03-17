#include <vector>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        for (int ind = n + m - 1; ind >= 0; --ind){
            int x = 0;
            if (i >= 0 && j >= 0){
                if (nums1[i] >= nums2[j]){
                    x = nums1[i];
                    --i;
                }
                else{
                    x = nums2[j];
                    --j;
                }
            }else if (i>=0){
                x = nums1[i];
                --i;
            }else{
                x = nums2[j];
                --j;
            }
            nums1[ind] = x;
        }
    }
};