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
public:
    vector<int> postorderTraversal(TreeNode* root) {
        findPostOrder(root);
        return ans;
    }
    vector<int>ans;
    void findPostOrder(TreeNode* rootNode){
        if(!rootNode){
            return;
        }
        findPostOrder(rootNode->left);
        findPostOrder(rootNode->right);
        ans.push_back(rootNode->val);
        
    }
};