class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {

        int rows=grid.size();
        int cols=grid[0].size();
        cout<<cols;
        int p=0;

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if (grid[i][j]==1){
                    if (i==0 || grid[i-1][j]==0){
                        p++;

                    }
                    if (i==rows-1 || grid[i+1][j]==0){
                        p++;

                    }
                    if (j==0 || grid[i][j-1]==0){
                        p++;

                    }
                    if (j==cols-1 || grid[i][j+1]==0){
                        p++;

                    }
                }

            }
        }
        return p;
    }
};