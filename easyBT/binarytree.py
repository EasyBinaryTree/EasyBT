from typing import List
from collections import deque


class TreeNode:
    def __init__(self,val,left=None,right=None)->None:   
        self.left=left
        self.right=right
        self.val=val
        

class BinaryTree:
    """Methods :
        1. SerializeTree
        2. DesializeTree
        3. VisualizeTree
        4. InOrderTraversal ,PostOrderTraversal, PreOrderTraversal
        5. LevelOrderTraversal
        6. Height
        7. MirrorTree
        8. NumberOfLeafNodes
        9. LeafNodes
        10. Diameter
    """
    
    def InOrderTraversal(self,root:TreeNode) -> List[int]:
        """return : List[int]\nobjective : InOrderTraversal will gives the inorder traversal of the binary tree
        """
        inoder_list=[]
        def inorder(root:TreeNode) -> None:
            if root:
                inorder(root.left)
                inoder_list.append(root.val)
                inorder(root.right)
        inorder(root)
        return inoder_list
    
    def PostOrderTraversal(self,root:TreeNode) -> List[int]:
        """return : List[int]\nobjective : PostOrderTraversal will gives the post order traversal of the binary tree
        """
        postorder_list=[]
        def postorder(root:TreeNode) -> None:
            if root:
                postorder(root.left)
                postorder(root.right)
                postorder_list.append(root.val)
        postorder(root)
        return postorder_list
    
    def PreOrderTraversal(self,root:TreeNode) -> List[int]:
        """return : List[int]\nobjective : PreOrderTraversal will gives the pre order traversal of the binary tree
        """
        preorder_list=[]
        def preorder(root:TreeNode) -> None:
            if root:
                preorder_list.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return preorder_list
    
    def LevelOrderTraversal(self,root:TreeNode)->List:
        """
        The fuction returns level order travesal of the binary tree
        
        Parameters :
                    root=TreeNode
        return : 
                 List[List[int]]
        Approach : 
                   Used Breadth first search algorithm
        Example :   

                     1             
                    / \            
                   2   3         => [[1],[2,3],[4,5,6]]  
                  /\   /          
                 4  5 6    
        """
        
        if not root:[]
        result=[]
        queue=[root]
        while queue:
            row=[]
            for _ in range(len(queue)):
                temp=queue.pop(0)
                row.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            result.append(row)
        return result
    
    # """def verticalOrderTraversal(self,root:TreeNode)->int:return"""
    
    def Diameter(self,root:TreeNode)->int:
        """
        The Function will returns the lenght of the diameter of the binary tree
        
        Parameters:
                    root=TreeNode
        return : 
                 int
        Defination: 
                    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
                    This path may or may not pass through the root.
        Approach : 
                    Using Depth First Search Algorithm
        """
        
        def diameter(root:TreeNode)->tuple(int):
            if root==None:
                return -1,0
            l_height,l_diameter=diameter(root.left)  
            r_height,r_diameter=diameter(root.right)
            return (max(l_height,r_height)+1,
                            max(l_height+r_height+2,l_diameter,r_diameter))        
        return diameter(root)[0]
    
    def Height(self,root:TreeNode)->int:
        """
        The Function will returns the height of the binary tree
        
        Parameters:
                    root=TreeNode
        return : 
                 int
        Defination: 
                    The height of a binary tree is the maximum distance from the root node to the leaf node.
        Approach : 
                    Using Depth First Search Algorithm
        """
        if root==None:
            return -1
        return max(self.Height(root.left),
                        self.Height(root.right))+1
        
    def MirrorTree(self,root:TreeNode)->None:
        """
        The Function will returns the height of the binary tree
        
        Parameters:
                    root=TreeNode
        return : 
                 int
        Defination: 
                    The height of a binary tree is the maximum distance from the root node to the leaf node.
        Approach : 
                    Using Depth First Search Algorithm
        """
        if root==None or (root.left==None and root.right==None):
            return
        r_x=root.right
        root.right=root.left
        root.left=r_x
        self.MirrorTree(root.left)
        self.MirrorTree(root.right)

    """def BottomView(self,root:TreeNode)->List[int]:
        return
    def TopView(self,root:TreeNode)->List[int]:
        return
    def LeftView(self,root:TreeNode)->List[int]:
        return
    def RightView(self,root:TreeNode)->List[int]:
        return"""
    
    def NumberOfLeafNodes(self,root:TreeNode)->int:
        if root==None:return 0
        if root and root.left==None and root.right==None:return 1
        return self.NumberOfLeafNodes(root.left)+self.NumberOfLeafNodes(root.right)
    
    def LeafNodes(self,root:TreeNode)->List[int]:
        """
        Parameters:
                    root=TreeNode
        return : 
                 List[int]
                 
        Defination:
                    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
                    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
        Approach : 
                    Using Depth First Search Algorithm
        """
        nodes=[]
        def dfs(root:TreeNode):
            if root==None:
                return
            if root and root.left==None and root.right==None:
                nodes.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return nodes
    
    
    def SerializeTree(self,root:TreeNode) -> List[int]:
        """
        Tree to list
        Parameters:
                    root=TreeNode
        return : 
                 List[int]
                 
        Defination:
                    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
                    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
        Approach : 
                    Using Breadth First Search Algorithm
        """
        if not root:return []
        queue=[root]
        result=[]
        while queue:
            temp=queue.pop(0)
            if temp:
                result.append(temp.val)
                queue.extend([temp.left,temp.right])
            else:
                result.append("*")
        i=len(result)-1  
        while result[i]=='*':
            result.pop()
            i-=1
        return result
    
    def DesializeTree(self,data:List[int]) -> TreeNode:
        """
        List To Binary Tree
        Parameters:
                    root=TreeNode
        return : 
                 List[int]
                 
        Defination:
                    Desialize is the process of converting 
        Approach : 
                    Using Breadth First Search Algorithm
        """
        if not data:return None
        tree=deque(data)
        root=TreeNode(tree.popleft())
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if tree:
                left_node=tree.popleft()
                if left_node!=None and left_node!='*':
                        node.left=TreeNode(left_node)
                        queue.append(node.left)
            if tree:    
                right_node=tree.popleft()
                if right_node!=None and right_node!="*":
                    node.right=TreeNode(right_node)
                    queue.append(node.right)
        return root
    
    def BuildBinaryTreeFromInOrderAndPostOrder(self,preorder: List[int], inorder: List[int])->TreeNode:
        if len(preorder)!=len(inorder):
            print("InOrder and PostOrder are not equal")
            return
        dict_={}
        preorder_index=0
        for i,e in enumerate(inorder):
            dict_[e]=i
        def buildTree(left:int,right:int)->TreeNode:
            nonlocal preorder_index
            if left>right:
                return
            index=dict_[preorder[preorder_index]]
            root=TreeNode(preorder[preorder_index])
            preorder_index+=1
            
            root.left=buildTree(left,index-1)
            root.right=buildTree(index+1,right)
            return root
        return buildTree(0,len(inorder)-1)
    
    def VisualizeTree(self,root:TreeNode)->None:
        height=self.Height(root)
        rows,cols=height+1,2**height+1
        mat=[["_"]*cols for _ in range(rows)]
        def buildMat(root:TreeNode,row:int,col:int)->None:
            if root==None:return
            if mat[row][col]=="_":
                mat[row][col]=str(root.val)
            else:
                if int(mat[row][col]):
                    mat[row][col]=mat[row][col]+","+str(root.val)
            if root.left:buildMat(root.left,row+1,col-1)
            if root.right:buildMat(root.right,row+1,col+1)
        buildMat(root,0,cols//2)
        for i in range(len(mat)):
            print(mat[i])
            print()
        





class BinarySearchTree(BinaryTree):
    """Methods :
        1. SerializeTree
        2. DesializeTree
        3. VisualizeTree
        4. InOrderTraversal ,PostOrderTraversal, PreOrderTraversal
        5. LevelOrderTraversal
        6. Height
        7. MirrorTree
        8. NumberOfLeafNodes
        9. LeafNodes
        10. Diameter
        11. searchInBST
        12. createBST / updateBST
        13. minValueNodeInBST
        14. maxValueNodeInBST
        15. deleteNode
    """
    
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
        """
        Create Binary search tree from unsorted list
        if root is not None then is will update your tree
        
        Parameters:
                data:List[int]
                root:TreeNode or root=None
        return : 
                root:TreeNode
        Approach : 
                 Using Recursion
        """
        if not len(data):
            return root
        if root==None:
            root=TreeNode(data[0])
        for i in data[1:]:
            root=self.insertInBST(root,i)   
        return root
        
    
    def insertInBST(self,root:TreeNode,element:int)->TreeNode:
        """
        Insert element in the Binary search tree 
        
        Parameters:
                data:List[int]
                root:TreeNode or root=None
        return : 
                root:TreeNode
        Approach : 
                 Using Recursion
        """
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
            root.left=self.deleteNode(root.left,target)
        elif root.val<target:
            root.right=self.deleteNode(root.right,target)
        else:
            
            # if root.left==None:
            #     temp=root.right
            #     root=None
            #     return temp
            # if root.right==None:
            #     temp=root.left
            #     root=None
            #     return temp
            # temp=self.minValueNodeInBST(root.right)
            # root.val=temp.val
            # root=self.deleteNode(root.right,temp.val)
            
            if root.left and root.right:
                temp=self.maxValueNodeInBST(root.left)
                root.val=temp.val
                root.left=self.deleteNode(root.left,temp.val)
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
                
                
        return root


            

"""
               [1,2,3,4,5,6]         [1,2,None,4,5,6]

                     1             |       1
                    / \            |      / 
                   2   3           |     2  
                  /\   /           |    / \
                 4  5 6            |   4   5    
                                   |  /
                                   | 6      
"""