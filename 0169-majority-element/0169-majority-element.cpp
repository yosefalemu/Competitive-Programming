class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int length_nums = nums.size();
        int middle_length_nums = nums.size()/2;
        unordered_map<int, int>dict1;
        for(int i = 0; i < nums.size();i++){
            dict1[nums[i]] ++;
        }
        int majority_ele = 0;
        for(auto item:dict1){
            if(item.second > middle_length_nums){
                majority_ele = item.first;
            }
        }
        return majority_ele;
    }
};