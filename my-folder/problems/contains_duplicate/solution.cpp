class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        set<int> s;
        auto it=nums.begin();
       

        while (it!=nums.end()){
            if (s.find(*(it))!=s.end()){
            return true;
            }
            s.insert(*(it));
            it++; 
        }
        return false;
        
    }
};