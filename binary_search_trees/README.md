# Binary Search Trees

- can be used to solve almost every data structures problem reasonably efficiently
    - efficient search for key
    - efficient locating of max and min elements
    - look for successor or predecessor of a search key
        - not necessarily present in the actual tree
    - enumerate the keys in a range in sorted order
- operations take up `O(h)` time, `h` is the height of the tree, which may be linear worst case, but a proper implementation can guaratee `log(n)`
    - red-black trees
    - AVL trees
- iterate thorugh elements in sorted order in linear time
- consider using both a hashtable AND a BST
- we may need to augment a BST to support most complicated data
    - number of elements in a range
- Global Property: each node's key is greater than the key at its left child and smaller then the key at its right child

## Prototypical Node

```python3
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
```

## Library

- `sortedcontainers` module
    - sorted list of sorted lists
    - square root time
- `bintrees` module

```python3
insert(e)
discard(e)
min_item()
max_item()
min_key()/max_key()
pop_min()
pop_max()
```

```python3
t = bintrees.RBTree([(5, 'Alfal), (2, 'Bravo')])
print(t[2])
t.min_item()
t.max_item()
t.min_key()
t.max_key()
t.discard(3)
t.pop_min()
t.pop_max()
```
