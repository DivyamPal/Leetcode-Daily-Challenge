class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        //initialize length of vector height
        //use two pointer approch
        int i=0,j=n-1;
        int area=0;
        int temp;
        while(i<j)
        {
            temp=min(height[i],height[j]);
            area=max(area,temp*(j-i));
            if(height[i]<height[j]) i++;
            else j--;
        }
        return area;
        
    }
};
