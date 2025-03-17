#include <vector>

using namespace std;


class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int max_free = 0, free = 0, ans = 0;
        for (int i=0; i<seats.size(); ++i){
            if (seats[i] == 0){
                free += 1; 
            }
            else {
                int tmp = (i - free) == 0 ? free : free / 2 + free % 2;
                free = 0;
                if (tmp > ans){
                    ans = tmp;
                }
            }
        }
        if (free > ans){
            ans = free;
        }
        return ans;
    }
};