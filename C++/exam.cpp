/*
Quetion
Given a preOrder and inOrder traversal of binary tree your task to print the postOrder traversal of the tree.
You are required to write the code in C++ which prints the node of the tree in a postorder fashion.

input 
4,2,5,1,3,6
1,2,4,5,3,6
Output 
4 5 2 6 3 1
*/
#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int findIndex(vector<int>& vec, int value) {
  for (int i = 0; i < vec.size(); i++) {
    if (vec[i] == value) {
      return i;
    }
  }
  return -1;
}


TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder, int preStart, int preEnd, int inStart, int inEnd) {
  if (preStart > preEnd || inStart > inEnd) return NULL ;

  int rootValue = preorder[preStart];
  TreeNode* root = new TreeNode(preStart);

  int rootValue = inorder[inStart]
  TreeNode* root =new TreeNode(inStart);

  int rootIndex = findIndex(inorder, rootValue);
  
  return root;

}

void postOrder(TreeNode* root) {
  if (root == NULL) return;

  postOrder(root->left);
  postOrder(root->right);

  cout << root->val << " ";
}
int main() {
  vector<int> preorder = {4, 2, 5, 1, 3, 6};
  vector<int> inorder = {1, 2, 4, 5, 3, 6};


  postOrder(root);
  cout << endl;

  return 0;
}


