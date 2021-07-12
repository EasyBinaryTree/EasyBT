
# EasyBT

Make Binary trees easy for everyone it is used to serialize-deserialize  binary trees and performs much more operations
1. SerializeTree (tree nodes to list )
2. DesializeTree (list to tree nodes )
3. Height (Finds height of the tree) and Diameter (Finds diameter of the tree)
4. InOrderTraversal,PostOrderTraversal,PreOrderTraversal
5. LevelOrderTraversal
6. MirrorTree
7. LeafNodes,NumberOfLeafNodes
8. VisualizeTree

## Installation
[![Python Version](https://img.shields.io/badge/python-3.0-brightgreen.svg)](https://python.org)

Use the package manager [pip](pypi.org/project/easybt/) to install easybt.

```bash
pip install easybt
```

## Usage

```python
from easybt.binarytree import BinaryTree

# Create Object
bt=BinaryTree()

# add nodes in list
nums=[1,2,None,None,5,6]

# it will return root node of the tree
root=bt.DesializeTree(nums)


```
## Examples

```python

               [1,2,3,4,5,6]         [1,2,None,4,5,6]

                     1                    1
                    / \                  / 
                   2   3                2  
                  /\   /               / \
                 4  5 6               4   5    
                                     /
                                    6      
```

# Documetation

#### To Read Documentation
```python

print(bt.SerializeTree.__doc__)

```
### DesializeTree
```python
from easybt.binarytree import BinaryTree

# Create Object
bt=BinaryTree()

# add nodes in list
nums=[100,500,20,10,30]

# it will return the root node of the tree

root=bt.DesializeTree(nums) 

              100                       
             /   \             
           500     20             
          /  \                              
         10   30 

```

### Visualize Tree

```python

VisualizeTree(root)

#it will print

"""
    ['_', '_', '1', '_', '_']

    ['_', '2', '_', '3', '_']

    ['4', '_','5,6', '_', '_']
"""

```
## BinarySearch Tree

11. searchInBST (finds element in the bst)
12. createBST (create bst)
13. minValueNodeInBST (finds min value in the bst)
14. maxValueNodeInBST (finds max value in the bst)
15. deleteNode (delete node from the bst)


```python
from easybt.binarytree import BinarySearchTree 

bst=BinarySearchTree()
```

### Creation 

```python

data=[100,500,20,10,30]

root=None

root=bst.createBST(data=data)


              100                       
             /   \             
           20     500             
          /  \                              
         10   30 
         
```

### Insertion


```python

 bst.insertInBST(root,40) or root=bst.insertInBST(root,40)


         100                                      100
        /   \         bst.insertInBST(40)        /    \
      20     500       --------->              20     500 
     /  \                                     /  \  
    10   30                                  10   30
                                                   \   
                                                   40
```

### Deletion

```python
bst.deleteNode(root,20)

              50                             50
            /    \      deleteNode(20)     /    \
          30      70       --------->     30     70 
         /  \    /  \                      \    /  \ 
       20   40  60   80                    40  60   80


bst.deleteNode(root,30)

             50                              50
           /    \       deleteNode(30)      /   \
          30     70       --------->      40     70 
            \    /  \                           /  \ 
            40  60   80                       60   80

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#### Contributors

1. [Samir Patil](https://github.com/samirpatil2000)