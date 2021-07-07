from typing import List
from collections import deque

class TreeNode:
    def __init__(self,val,left=None,right=None)->None:   
        self.left=left
        self.right=right
        self.val=val
        

class BinaryTree:
    
    def InOrderTraversal(self,root:TreeNode) -> List:
        inoder_list=[]
        def inorder(root:TreeNode) -> None:
            if root:
                inorder(root.left)
                inoder_list.append(root.val)
                inorder(root.right)
        inorder(root)
        return inoder_list
    
    def PostOrderTraversal(self,root:TreeNode) -> List:
        postorder_list=[]
        def postorder(root:TreeNode) -> None:
            if root:
                postorder(root.left)
                postorder(root.right)
                postorder_list.append(root.val)
        postorder(root)
        return postorder_list
    
    def PreOrderTraversal(self,root:TreeNode) -> List:
        preorder_list=[]
        def preorder(root:TreeNode) -> None:
            if root:
                preorder_list.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return preorder_list
    
    def LevelOrderTraversal(self,root:TreeNode)->List:
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
    
    """def verticalOrderTraversal(self,root:TreeNode)->int:return"""
    
    def Diameter(self,root:TreeNode)->int:
        def diameter(root:TreeNode)->tuple(int):
            if root==None:
                return -1,0
            l_height,l_diameter=diameter(root.left)  
            r_height,r_diameter=diameter(root.right)
            return (max(l_height,r_height)+1,
                            max(l_height+r_height+2,l_diameter,r_diameter))        
        return diameter(root)[0]
    
    def Height(self,root:TreeNode)->int:
        if root==None:
            return -1
        return max(self.Height(root.left),
                        self.Height(root.right))+1
        
    def MirrorTree(self,root:TreeNode)->None:
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