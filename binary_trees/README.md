# Binary Trees

- search trees
- appropriate when dealing with hierarchies

## Definitions

- A tree is either
    1. empty
    2. a node with a left subtree and a right subtree
- search path
- ancestor
- descendant
- leaf
- depth
- height
- full binary tree
- perfect binary tree
- complete binary tree

## Canonial Node

```python3
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
```

## Key Computations
- traversal
    - inorder
    - preorder
    - postorder

## Points to Consider
- recursive algorithms work well with the structural definition of trees
    - consider space implicitly allocated for the call stack
- consider using existing nodes for `O(1)` space complexity algorithms
- consider including a parent pointer
- do not mistaken a single child node as a leaf node
