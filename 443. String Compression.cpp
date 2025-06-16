class Solution {
public:
    int compress(vector<char>& chars) {
        vector<char> s;
        int n = chars.size(), start = 0, count = 1;
        bool flag = false;
        for (int i=1; i<=n; ++i) {
            if (i != n && chars[i] == chars[i-1]) {
                count += 1;
            } else {
                s.push_back(chars[i-1]);
                auto it = s.end();
                if (count > 1) {
                    string scount = to_string(count);
                    s.insert(it, scount.begin(), scount.end());
                }
                count = 1;
            }
        }
        chars = s;
        return chars.size();
    }
};