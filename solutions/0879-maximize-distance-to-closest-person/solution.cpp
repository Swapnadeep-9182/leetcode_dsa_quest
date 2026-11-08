class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int n = seats.size();
        int prev = -n;
        vector<int> ans(n, 0);

        for (int i = 0; i < n; i++) {
            if (seats[i] == 1) {
                prev = i;
            }
            ans[i] = i - prev;
        }

        prev = 2 * n;
        for (int j = n - 1; j >= 0; j--) {
            if (seats[j] == 1) {
                prev = j;
            }
            ans[j] = min(prev - j, ans[j]);
        }

        int res = 0;
        for (int d : ans) {
            res = max(res, d);
        }

        return res;
    }
};
