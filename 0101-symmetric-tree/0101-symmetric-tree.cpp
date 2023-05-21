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
    bool isSymmetric(TreeNode* root) {
        return checkSymmetric(root->left,root->right);
        
    }
    bool checkSymmetric(TreeNode* leftNode, TreeNode* rightNode){
        if(leftNode == nullptr && rightNode == nullptr){
            return true;
        }
        if(leftNode == nullptr && rightNode != nullptr || leftNode != nullptr && rightNode ==nullptr){
            return false;
        }
        if(leftNode->val != rightNode->val){
            return false;
        }
        return checkSymmetric(leftNode->left,rightNode->right)&&checkSymmetric(leftNode->right,rightNode->left);
    }
};