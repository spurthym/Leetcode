class Solution {
public:
    int missingNumber(vector<int>& nums) {


        int n=nums.size();
        int i=0;


        while (i<=n){
            bool flag=false;

            for (int num: nums){
                if (i==num){
                    flag=true;
                    break;
                }
            }
            if (flag==false){
                return i;
            }
            i++;
            }
            return -1;
        }
        



        
    
};