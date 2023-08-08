class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i=0;
        int n=nums.size();
        int j=0;
        int temp=0;
        while (i<n){
            j=nums[i]-1;
            if (nums[i]!=nums[j]){
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
            }
            else{
                i++;
            }
        }
        vector<int> res;
        int k=0;

        for (k=0;k<n;k++){
            if (nums[k]!=k+1){
                break;
            }
        }
        return nums[k];
    }
};