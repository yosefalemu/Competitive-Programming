/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    TreeNode* rec(int left, int right, vector<int>nums){
        if(left > right){
            return NULL;
        }
        int mid = left + (right - left)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = rec(left, mid-1, nums);
        root->right = rec(mid + 1, right, nums);
        return root;
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        ListNode* curr = head;
        vector<int>temp;
        while(curr){
            temp.push_back(curr->val);
            curr = curr->next;
        }
        return rec(0, temp.size()-1,temp);
    }
};