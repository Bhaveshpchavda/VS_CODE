#include <iostream>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Helper function to find the index of a value in a vector
int findIndex(vector<int>& vec, int value) {
  for (int i = 0; i < vec.size(); i++) {
    if (vec[i] == value) {
      return i;
    }
  }
  return -1;
}

// Function to build a binary tree from preorder and inorder traversals
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder, int preStart, int preEnd, int inStart, int inEnd) {
  if (preStart > preEnd || inStart > inEnd) return NULL;

  // Create the root node using the value from the preorder traversal
  int rootValue = preorder[preStart];
  TreeNode* root = new TreeNode(rootValue);

  // Find the index of the root value in the inorder traversal
  int rootIndex = findIndex(inorder, rootValue);

  // Recursively build the left and right subtrees
  root->left = buildTree(preorder, inorder, preStart + 1, preStart + rootIndex - inStart, inStart, rootIndex - 1);
  root->right = buildTree(preorder, inorder, preStart + rootIndex - inStart + 1, preEnd, rootIndex + 1, inEnd);

  return root;
}

// Recursive function to print the postorder traversal of a binary tree
void postOrder(TreeNode* root) {
  if (root == NULL) return;

  // Recursively traverse the left and right subtrees
  postOrder(root->left);
  postOrder(root->right);

  // Print the value of the current node
  cout << root->val << " ";
}

int main() {
  // Input preorder and inorder traversals
  vector<int> preorder = {4, 2, 5, 1, 3, 6};
  vector<int> inorder = {1, 2, 4, 5, 3, 6};

  // Build the tree from the preorder and inorder traversals
  TreeNode* root = buildTree(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);

  // Print the postorder traversal of the tree
  postOrder(root);
  cout << endl;

  return 0;
}
