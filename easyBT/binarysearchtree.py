from binarytree import TreeNode
from typing import List
from binarytree import BinaryTree,TreeNode

class BinarySearchTree(BinaryTree):
    
    def PostOrderToBinarySearchTree(self,postorder:List[int])->TreeNode:
        return
    def PreOrderToBinarySearchTree(self,preorder:List[int])->TreeNode:
        return
    
    def searchInBST(self,root:TreeNode,target:int)->TreeNode:
        if root==None or root.val==target:
            return root
        if root.val > target:
            return self.searchInBST(root.left,target)
        return self.searchInBST(root.right,target)
    
    def createBST(self,data:List[int],root=None)->TreeNode:
        if not len(data):
            return root
        if root==None:
            root=TreeNode(data[0])
        for i in data[1:]:
            root=self.insertInBST(root,i)
        
        return root
        
    
    def insertInBST(self,root:TreeNode,element:int)->TreeNode:
        if root==None:
            return TreeNode(val=element)
        else:
            if root.val==element:
                print("Element Already Present In BST")
                return root
            if root.val>element:
                root.left=self.insertInBST(root.left,element)
            else:
                root.right=self.insertInBST(root.right,element)
            return root
        
    def minValueNodeInBST(self,root:TreeNode)->TreeNode:
        if root==None:return root
        temp=root
        while temp and temp.left:
            temp=temp.left
        return temp
    def maxValueNodeInBST(self,root:TreeNode)->TreeNode:
        if root==None:return root
        temp=root
        while temp and temp.right:
            temp=temp.right
        return temp
    
    def deleteNode(self,root:TreeNode,target:int)->TreeNode:
        if root==None:
            return root
        if root.val>target:
            root.right=self.deleteNode(root.left,target)
        elif root.val<target:
            root.left=self.deleteNode(root.right,target)
        else:
            if root.left==None:
                temp=root.right
                root=None
                return temp
            if root.right==None:
                temp=root.left
                root=None
                return temp
            temp=self.minValueNodeInBST(root.right)
            root.val=temp.val
            root.right=self.deleteNode(root.right,temp.val)
        return root
