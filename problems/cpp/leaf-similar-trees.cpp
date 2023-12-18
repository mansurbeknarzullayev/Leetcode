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
    vector<int>go(TreeNode *node){
        vector<int>v;
        if(node){
            if(node->left || node->right){
                vector<int>v1 = go(node->left);
                vector<int>v2 = go(node->right);
                for(int i = 0; i < v2.size(); i++){
                    v1.push_back(v2[i]);
                }               
                return v1;
            }
            else{
                return vector<int>(1, node->val);
            }
        }
        else{
            return v;
        }
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        return go(root1) == go(root2);
    }
};