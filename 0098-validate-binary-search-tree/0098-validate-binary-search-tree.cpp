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
    bool isBST(TreeNode* root,long long mini,long long maxi){
        //Base Case
        if(root == NULL) return true;
        if(root->val>mini && root->val<maxi){
           bool left=isBST(root->left,mini,root->val);
           bool right=isBST(root->right,root->val,maxi);
           return left && right;
        }
        else return false;
    }
    bool isValidBST(TreeNode* root) {
        long long int mini=-1000000000000,maxi=1000000000000;
        return isBST(root,mini,maxi);
    }
};