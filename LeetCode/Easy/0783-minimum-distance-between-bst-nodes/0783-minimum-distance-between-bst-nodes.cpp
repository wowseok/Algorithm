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

    long long prev = -INT_MAX;
    long long result = INT_MAX;
    int minDiffInBST(TreeNode* root) {
        if (root->left) minDiffInBST(root->left);

        result = min(result, root->val - prev);
        prev = root->val;

        if(root->right) minDiffInBST(root->right);

        return result;
    }
};