from binarytree import BinaryTree
        
bt=BinaryTree()
x=[1,2,3,4,5,6]
root=bt.DesializeTree(x)
print(bt.InOrderTraversal(root))
print(bt.PreOrderTraversal(root))
print(bt.SerializeTree(root))
print(bt.InOrderTraversal(root))
print(bt.LevelOrderTraversal(root))