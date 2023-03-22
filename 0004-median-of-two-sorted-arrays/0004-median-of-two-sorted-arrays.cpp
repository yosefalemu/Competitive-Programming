class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1=nums1.size();
        int n2=nums2.size();
        int n=n1+n2;
        int i=0, j=0, count=0;
        int prev=0;
        int temp=0;

        while(i<n1 && j<n2){
            prev=temp;
            count++;
            if(nums1[i]<nums2[j]){
                temp=nums1[i];
                i++;
            }
            else if(nums1[i]>nums2[j]){
                temp=nums2[j];
                j++;
            }
            else{
                temp=nums1[i];
                if(count<n/2+1)
                prev=temp;
                i++;
                j++;
                count++;
            }
            if(count>=n/2+1){
                if(n%2!=0)
                return temp;
                else
                return (temp+prev)/2.0;
            }
        }
        while(i<n1){
            prev=temp;
            temp=nums1[i];
            i++;
            count++;
            if(count>=(n)/2+1){
                if(n%2!=0)
                return temp;
                else
                return (temp+prev)/2.0;
            }
        }
        while(j<n2){
            prev=temp;
            temp=nums2[j];
            j++;
            count++;
            
            if(count>=(n)/2+1){
                if(n%2!=0)
                return temp;
                else
                return (prev+temp)/2.0;
            }
        }
        return 0;
    }

};