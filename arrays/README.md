# Arrays

- arrays often have brute force solutions using O(n) space
    - there are solutions that use the array itself to reduce space complexity to O(1)
- consider processing the digits from the back or reversing the array
- operate on subarrays
- do not worry about preserving integrity of the array (sortedness, equal entries together, etc) until it is time to return
- arrays are good data structure if distribution of elements are known in advance
    - using boolean array to represent subset of integers 1, ..., n
- use parallel logic on rows and columns for 2D arrays
- attempt to simulate the specifications than to analytically solve for the result
    - rather than writing a formula for the i-th entry in spiral order in n x n matrix, just compute output from beginning

# Libraries

## Initialization
```python3
list  # dynamically resized array
[1]
[1] + [0]*10
list(range(100))
```

## Basic Operations
```python3
len
list.append
list.remove
list.insert

a in A
```

## Copies
```python3
B = A
B = list(A)
copy.copy
copy.deepcopy
```

## Key Methods
```python3
min
max
bisect.bisect(A, 6) # locate insertion point for 6 in A to maintain sorted order, defaults to right if element exists
bisect.bisect_left(A, 6)
bisect.bisect_right(A, 6)
list.reverse
reversed
list.sort
sorted
del A[i]
del A[i:j]
```

## Slicing
```python3
A[i:j:k]
A[k:] + A[:k]
B = A[:]
```

## List Comprehension
```python3
[x**2 for x in range(6)]
[x**3 for x in range(6) if x % 2 == 0]
# multiple levels of scoping
[(x, y) for x in A for y in B]
[x for row in M for x in row]
```

## Immutability
```python3
tuple  # immutable array
```
