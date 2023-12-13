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
    int depth = 0;
    int sum = 0;
    void go(TreeNode *node, int dep){
        if(node){
            if(dep > depth){
                depth = dep;
                sum = node->val;
            }
            else if(dep == depth){
                sum += node->val;
            }
            go(node->left, dep + 1);
            go(node->right, dep + 1);
        }
    }
    int deepestLeavesSum(TreeNode* root) {
        go(root, 0);
        return sum;
    }
};