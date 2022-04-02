class Solution {
public:
    bool validPalindrome(string s) {
        int count1=0,count2=0;
        int n=s.length();
        int end=n-1,start=0;
        while(start<end)
        {
            if(s[start]==s[end])
            {
                start++;
                end--;
            }
            else 
            {
                start++;
                count1++;
            }
        }
        end=n-1;start=0;
        while(start<end)
        {
            if(s[start]==s[end])
            {
                start++;
                end--;
            }
            else 
            {
                end--;
                count2++;
            }
        }
        if((count1==1||count2==1)||(count1==0&&count2==0))
        {
            return true;
        }
        else return false;
        
    }
};
