# Sorting

- make subsequent steps in an algorithm simpler
    - consider using library sort (with custom comparator)
- design a custom sorting routine
    - consider using an auxiliary data structure like a BST, heap, or array indexed by values
- a natural reason to sort is if the inputs have a natural ordering, or if it speeds up searching
- for specialized input, we may sort in `O(n)` time instead of `O(logn)`
- sorting can often be implemented in less space than required by a brute-force approach
- it may not be obvious what exactly should be sorted
    - collection of intervals sorted by starting points or endpoints?

## Sorting Libraries

```python3
sort(key=None, reverse=False)  # stable in-place sort for list objects
sorted(it, key=None, reverse=False)  # takes an iterable and returns a new list containing all items from the iterable in ascending order
```
