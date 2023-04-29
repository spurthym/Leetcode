class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int,int> d;
        int n=nums.size();
        vector<int> res;

        for(int i=0;i<=n;i++){
            if (d.find(nums[i]) !=d.end()){
                res.push_back(i);
                res.push_back(d[nums[i]]);
                return res;
            }

            d[target-nums[i]]=i;
        }
        return res;
    }
};