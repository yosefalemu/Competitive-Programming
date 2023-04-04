class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int length_nums = nums.size();
        int middle_length_nums = nums.size()/2;
        
        sort(nums.begin(),nums.end());
        return nums[middle_length_nums];
    }
};