
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;

        if (intervals.empty()) {
            return res;
        }

        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] <= end) {
                // Merge overlapping intervals
                end = max(intervals[i][1], end);
            } else {
                // Non-overlapping interval found, add the merged interval to the result
                res.push_back({start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }

        // Add the last merged interval to the result
        res.push_back({start, end});

        return res;
    }
};
