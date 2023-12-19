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
    int go(TreeNode *node, int mx){
        if(node){
            return (node->val >= mx) + go(node->left, max(node->val, mx)) + go(node->right, max(mx, node->val));
        }
        else{
            return 0;
        }
    }
    int goodNodes(TreeNode* root) {
        return go(root, -100000);
    }
};