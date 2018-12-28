# Heaps

- special type of binary tree
    - complete binary tree
- heap property
    - key at each node is at least as great as the keys stored at its children
- max-heap can be implemented as an array
- operations
    - insertion `O(log n)`
    - max lookup `O(1)`
    - deletion `O(log n)`
    - key lookup `O(n)`
- sometimes referred to as a priority queue
    - each element has "priority" associated with it
    - deletion removes element with highest priority
- min-heap is similar
- use a heap when all you care about is largest or smallest elements
    - k largest or k smallest elements
    - max-heap or min-heap

## Libraries

```python3
heapq.heapify(L)
heapq.nlargest(k, L)
heapq.nsmallest(k, L)
heapq.heappush(h, e)
heapq.heappop(h)
heapq.heappushpop(h, a)  # pushes a on heap then pops and returns smallest element
h[0]
```

### NOTE

- `heapq` only provides min-heap functionality
    - build max-heap on integers or floats by inserting negative values
- for objects, implement `__lt()__` appropriately
