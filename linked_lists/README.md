# Linked Lists

## Canonical Node and Methods
```python3
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# O(n)
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

# O(1)
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# O(1)
def delete_after(node):
    node.next = node.next.next
```

# Key Points
- clean code is often most important
- consider using a dummy head
- do not forget to update the next pointer
- consider using two iterators
    - one ahead of the other
    - one advancing quicker than the other
