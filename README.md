
# EasyBT

Make Binary trees easy for everyone it is used to serialize-deserialize  binary trees and performs much more operations
1. Serialize (tree nodes to list )
2. Deserialize (list to tree nodes )
3. Height (Finds height of the tree) and Diameter (Finds diameter of the tree)
4. InOrderTraversal,PostOrderTraversal,PreOrderTraversal
5. LevelOrderTraversal
6. MirrorTree
7. LeafNodes,NumberOfLeafNodes

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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#### Contributors

1. [Samir Patil](https://github.com/samirpatil2000)