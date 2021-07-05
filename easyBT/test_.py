from binarytree import BinaryTree  
 
bt=BinaryTree()
x=[1,2,3,4,5,6]
root=bt.DesializeTree(x)
# print(bt.InOrderTraversal(root))
# print(bt.PreOrderTraversal(root))
# print(bt.SerializeTree(root))
# print(bt.InOrderTraversal(root))
print(bt.LevelOrderTraversal(root))


# python3 -m pip install --user --upgrade setuptools wheel
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python3 -m twine upload --https://github.com/EasyBinaryTree/EasyBT.git https://test.pypi.org/legacy/ dist/*


# twine upload --skip-existing dist/*