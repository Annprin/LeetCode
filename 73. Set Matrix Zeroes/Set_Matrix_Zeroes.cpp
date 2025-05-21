#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<bool> cols(m), rows(n);
        for (int i=0; i<n; ++i) {
            for (int j=0; j<m; ++j) {
                if (matrix[i][j] == 0) {
                    cols[j] = 1;
                    rows[i] = 1;
                }
            }
        }

        for (int i=0; i<n; ++i) {
            for (int j=0; j<m; ++j) {
                if (rows[i] || cols[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};